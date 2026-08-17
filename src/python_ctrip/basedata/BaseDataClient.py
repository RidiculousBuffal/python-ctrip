from __future__ import annotations

import asyncio
import logging
from typing import Any
from uuid import uuid4

import httpx

from ..BaseClient import BaseClient
from ..basedata.model import (
    Authentification,
    FlightSearchResponse,
    POICondition,
    PrefectureLevelCityCondition,
    ProvinceCondition,
    QueryAllPOIInfoRequestType,
    QueryAllPOIInfoResponseType,
    SearchRequest,
    TicketRequest,
    TicketResponse,
)


class BaseDataClient(BaseClient):
    API_BASE_URL = "https://ct.ctrip.com"
    TICKET_PATH = "/SwitchAPI/Order/Ticket"
    COUNTRY_PATH = "/switchAPI/basedata/v2/getcountry"
    POI_PATH = "/switchapi/basedata/v2/queryAllPOIInfo"
    POI_RATE_LIMIT_RETRY_COUNT = 5
    POI_RATE_LIMIT_RETRY_DELAY_SECONDS = 60

    def __init__(
        self,
        transport: httpx.AsyncBaseTransport | None = None,
        *,
        corporate_id: str | None = None,
        app_key: str | None = None,
        app_security: str | None = None,
        sub_account_name: str | None = None,
    ):
        super().__init__(
            corporate_id=corporate_id,
            app_key=app_key,
            app_security=app_security,
            sub_account_name=sub_account_name,
        )
        self.transport = transport
        self.logger = logging.getLogger("python.ctrip.BaseDataClient")

    def build_ticket_request(
        self,
        app_key: str | None = None,
        app_security: str | None = None,
    ) -> TicketRequest:
        return TicketRequest(
            appKey=app_key or self.XIECHEN_APP_KEY,
            appSecurity=app_security or self.XIECHEN_APP_SECURITY,
        )

    def build_auth(
        self,
        ticket: str,
        app_key: str | None = None,
    ) -> Authentification:
        return Authentification(
            AppKey=app_key or self.XIECHEN_APP_KEY,
            Ticket=ticket,
        )

    def build_country_request(
        self,
        ticket: str,
        request_id: str | None = None,
        locale: str = "zh-CN",
        app_key: str | None = None,
    ) -> SearchRequest:
        return SearchRequest(
            requestId=request_id or str(uuid4()),
            locale=locale,
            auth=self.build_auth(ticket=ticket, app_key=app_key),
        )

    def build_query_all_poi_info_request(
        self,
        country_id: int,
        ticket: str,
        app_key: str | None = None,
        province_ids: str | None = None,
        province_names: str | None = None,
        prefecture_level_city_ids: str | None = None,
        prefecture_level_city_names: str | None = None,
        return_district: bool | None = True,
        return_county: bool | None = True,
        return_airport: bool | None = True,
        return_train_station: bool | None = True,
        return_bus_station: bool | None = True,
        start_date: str | None = None,
    ) -> QueryAllPOIInfoRequestType:
        province_conditions = None
        poi_conditions = None
        if start_date is None:
            prefecture_level_city_conditions = PrefectureLevelCityCondition(
                prefectureLevelCityIds=prefecture_level_city_ids,
                prefectureLevelCityNames=prefecture_level_city_names,
                returnDistrict=return_district,
                returnCounty=return_county,
            )
            province_conditions = ProvinceCondition(
                provinceIds=province_ids,
                provinceNames=province_names,
                prefectureLevelCityConditions=prefecture_level_city_conditions,
            )
            poi_conditions = POICondition(
                returnAirport=return_airport,
                returnTrainStation=return_train_station,
                returnBusStation=return_bus_station,
            )

        return QueryAllPOIInfoRequestType(
            auth=self.build_auth(ticket=ticket, app_key=app_key),
            countryId=country_id,
            provinceConditions=province_conditions,
            poiConditions=poi_conditions,
            startDate=start_date,
        )

    async def get_ticket(
        self,
        app_key: str | None = None,
        app_security: str | None = None,
    ) -> str | None:
        payload = self.build_ticket_request(
            app_key=app_key,
            app_security=app_security,
        )
        async with httpx.AsyncClient(
            base_url=self.API_BASE_URL,
            limits=self.limits,
            timeout=self.timeout,
            transport=self.transport,
        ) as client:
            response = await client.post(
                self.TICKET_PATH,
                json=payload.model_dump(exclude_none=True),
            )
            response.raise_for_status()
            return TicketResponse.model_validate(response.json()).Ticket

    async def get_country_list_raw(
        self,
        ticket: str | None = None,
        request_id: str | None = None,
        locale: str = "zh-CN",
        app_key: str | None = None,
    ) -> dict[str, Any]:
        actual_ticket = ticket or await self.get_ticket(app_key=app_key)
        payload = self.build_country_request(
            ticket=actual_ticket or "",
            request_id=request_id,
            locale=locale,
            app_key=app_key,
        )
        async with httpx.AsyncClient(
            base_url=self.API_BASE_URL,
            limits=self.limits,
            timeout=self.timeout,
            transport=self.transport,
        ) as client:
            response = await client.post(
                self.COUNTRY_PATH,
                json=payload.model_dump(exclude_none=True),
            )
            response.raise_for_status()
            raw_response = response.json()
            FlightSearchResponse.model_validate(raw_response)
            return raw_response

    async def query_all_poi_info_raw(
        self,
        country_id: int,
        province_ids: str | None = None,
        province_names: str | None = None,
        prefecture_level_city_ids: str | None = None,
        prefecture_level_city_names: str | None = None,
        return_district: bool | None = True,
        return_county: bool | None = True,
        return_airport: bool | None = True,
        return_train_station: bool | None = True,
        return_bus_station: bool | None = True,
        start_date: str | None = None,
    ) -> dict[str, Any]:
        ticket = await self.get_ticket(app_key=self.XIECHEN_APP_KEY)
        if not ticket:
            return {}
        payload = self.build_query_all_poi_info_request(
            country_id=country_id,
            ticket=ticket ,
            app_key=self.XIECHEN_APP_KEY,
            province_ids=province_ids,
            province_names=province_names,
            prefecture_level_city_ids=prefecture_level_city_ids,
            prefecture_level_city_names=prefecture_level_city_names,
            return_district=return_district,
            return_county=return_county,
            return_airport=return_airport,
            return_train_station=return_train_station,
            return_bus_station=return_bus_station,
            start_date=start_date,
        )
        async with httpx.AsyncClient(
            base_url=self.API_BASE_URL,
            limits=self.limits,
            timeout=self.timeout,
            transport=self.transport,
        ) as client:
            for attempt in range(self.POI_RATE_LIMIT_RETRY_COUNT + 1):
                response = await client.post(
                    self.POI_PATH,
                    json=payload.model_dump(exclude_none=True),
                )
                if response.status_code == httpx.codes.TOO_MANY_REQUESTS:
                    if attempt == self.POI_RATE_LIMIT_RETRY_COUNT:
                        response.raise_for_status()
                    self.logger.warning(
                        "query_all_poi_info_raw hit 429, retrying in %s seconds "
                        "(attempt %s/%s)",
                        self.POI_RATE_LIMIT_RETRY_DELAY_SECONDS,
                        attempt + 1,
                        self.POI_RATE_LIMIT_RETRY_COUNT,
                    )
                    await asyncio.sleep(self.POI_RATE_LIMIT_RETRY_DELAY_SECONDS)
                    continue

                response.raise_for_status()
                raw_response = response.json()
                QueryAllPOIInfoResponseType.model_validate(raw_response)
                return raw_response

    async def fetch_full_geo_snapshot(
        self,
        country_id: int,
        locale: str = "zh-CN",
        app_key: str | None = None,
    ) -> dict[str, Any]:
        ticket = await self.get_ticket(app_key=app_key)
        country_response = await self.get_country_list_raw(
            ticket=ticket,
            locale=locale,
            app_key=app_key,
        )
        poi_response = await self.query_all_poi_info_raw(
            country_id=country_id,
        )
        snapshot = {
            "countryId": country_id,
            "countryListResponse": country_response,
            "poiResponse": poi_response,
        }
        self.logger.info("Fetched full geo snapshot for country_id=%s", country_id)
        return snapshot
