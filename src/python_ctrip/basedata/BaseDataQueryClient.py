import asyncio
import json
import os.path
from typing import Any

from ..basedata import BaseDataClient
from ..basedata.model import Country, QueryAllPOIInfoResponseType
import logging

from ..exception.NoDataException import NoDataException


class BaseDataQueryClient:
    _NO_DATA = object()
    _FALLBACK_COUNTRY_DATA_FILES = {
        1: "中国.json",
        3: "新加坡.json",
        9: "阿联酋.json",
        15: "澳大利亚.json",
        28: "德国.json",
        31: "法国.json",
        42: "韩国.json",
        43: "荷兰.json",
        47: "加拿大.json",
        66: "美国.json",
        78: "日本.json",
        80: "瑞士.json",
        109: "英国.json",
        106:"意大利.json"
    }

    def __init__(self, client:BaseDataClient):
        self.queryClient = client
        self.country_map:dict[str,Country]={}
        self._query_cache: dict[tuple[int, str], QueryAllPOIInfoResponseType | object] = {}
        self._inflight_queries: dict[tuple[int, str], asyncio.Task[QueryAllPOIInfoResponseType]] = {}
        self._init_country_list()
        self.logger =  logging.getLogger("python.ctrip.BaseDataQueryClient")
        self.china_county_map: dict[str, list[str]] = {}
        self.country_fallback_maps: dict[int, dict[str, list[str]]] = {}
        self._init_fallback_country_maps()


    def _init_country_list(self):
        json_path = os.path.join(str(os.path.dirname(__file__)),"data/country_list.json")
        with open(json_path) as f:
            data = json.load(f)
            for country in data.get("countryList",[]):
                self.country_map[country.get("name")] = Country.model_validate(country)

    def _init_fallback_country_maps(self):
        data_dir = os.path.join(str(os.path.dirname(__file__)), "data")
        for country_id, filename in self._FALLBACK_COUNTRY_DATA_FILES.items():
            json_path = os.path.join(data_dir, filename)
            with open(json_path) as f:
                self.country_fallback_maps[country_id] = json.load(f)

        self.china_county_map = self.country_fallback_maps.get(1, {})

    def _checkQueryResult(self,queryResult:dict[str,Any]):
        if not queryResult.get("status", {}).get("success", False):
            return False
        return True

    def export_query_cache_to_json(self, json_path: str):
        cache_entries: list[dict[str, Any]] = []
        for (country_id, normalized_name), cached_value in self._query_cache.items():
            if cached_value is self._NO_DATA:
                continue

            cache_entries.append({
                "country_id": country_id,
                "normalized_name": normalized_name,
                "data": cached_value.model_dump(mode="json"),
            })

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(cache_entries, f, ensure_ascii=False, indent=2)

    def import_query_cache_from_json(self, json_path: str):
        with open(json_path, encoding="utf-8") as f:
            cache_entries = json.load(f)

        restored_cache: dict[tuple[int, str], QueryAllPOIInfoResponseType | object] = {}
        for entry in cache_entries:
            cache_key = (entry["country_id"], entry["normalized_name"])
            restored_cache[cache_key] = QueryAllPOIInfoResponseType.model_validate(entry["data"])

        self._query_cache = restored_cache

    async def _query(self,country_id:int,name:str):
        # 尝试 province
        res1 = await self.queryClient.query_all_poi_info_raw(country_id=country_id, province_names=name)
        if self._checkQueryResult(res1):
            return QueryAllPOIInfoResponseType.model_validate(res1)
        self.logger.warning("访问 country_id=%s, province_name=%s 时候未找到信息，准备退回到city_name,districtName查询", country_id,
                            name)
        res2 = await self.queryClient.query_all_poi_info_raw(country_id=country_id, prefecture_level_city_names=name)
        if self._checkQueryResult(res2):
            return QueryAllPOIInfoResponseType.model_validate(res2)

        return None
    def _normalize_name(self, name: str) -> str:
        if name == '中国香港':
            return '香港'

        if name == '中国澳门':
            return '澳门'

        if name == '中国台湾':
            return '台湾'

        return name

    async def _query_from_fallback_map(self, country_id: int, name: str):
        fallback_map = self.country_fallback_maps.get(country_id)
        if not fallback_map:
            return None

        candidate_names = [name]
        if country_id == 1:
            candidate_names.append(name.replace('县', ''))
            candidate_names.append(name.replace('市',''))
            candidate_names.append(name.replace('市区',''))


        region_names: list[str] | None = None
        for candidate_name in candidate_names:
            region_names = fallback_map.get(candidate_name)
            if region_names:
                break

        if not region_names:
            return None

        merged_result = await self._query(country_id, region_names[0])
        if not merged_result:
            return None

        for region_name in region_names[1:]:
            next_result = await self._query(country_id, region_name)
            if next_result and next_result.dataList:
                merged_result.dataList.extend(next_result.dataList)

        return merged_result

    async def _query_with_fallback(self, country_id: int, name: str):
        res = await self._query(country_id,name)
        if res:
            return res
        self.logger.warning("访问 country_id=%s, prefecture_level_city_names=%s 时候未找到信息,准备检查是否名字中含有 市，市区 等词语，准备去掉重试", country_id, name)
        if '市区' in name:
            res2 = await self._query(country_id,name.replace("市区",''))
            if res2:
                return res2

        if '市' in name:
            res3 = await self._query(country_id,name.replace('市',''))
            if res3:
                return res3

        self.logger.warning("访问 country_id=%s, prefecture_level_city_names=%s 时候未找到信息,准备查询县级市信息", country_id, name)
        res4 = await self._query_from_fallback_map(country_id, name)
        if res4:
            return res4
        raise NoDataException(name)

    async def query(self,country_id:int,name:str):
        normalized_name = self._normalize_name(name)
        cache_key = (country_id, normalized_name)

        cached = self._query_cache.get(cache_key)
        if cached is self._NO_DATA:
            raise NoDataException(normalized_name)
        if cached is not None:
            return cached.model_copy(deep=True)

        inflight = self._inflight_queries.get(cache_key)
        if inflight is not None:
            return (await inflight).model_copy(deep=True)

        task = asyncio.create_task(self._query_with_fallback(country_id, normalized_name))
        self._inflight_queries[cache_key] = task
        try:
            result = await task
        except NoDataException:
            self._query_cache[cache_key] = self._NO_DATA
            raise
        except Exception:
            raise
        else:
            self._query_cache[cache_key] = result
            return result.model_copy(deep=True)
        finally:
            self._inflight_queries.pop(cache_key, None)
