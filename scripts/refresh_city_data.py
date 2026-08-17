"""Refresh the county/district to prefecture-level-city lookup files.

Run from the repository root after installing the package, for example::

    python scripts/refresh_city_data.py --country 中国

The API credentials are read from the same environment variables as
``BaseDataClient``.  ``.env`` is loaded when python-dotenv is available.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
from pathlib import Path
from typing import Iterable

from dotenv import load_dotenv

from python_ctrip.basedata import BaseDataClient, QueryAllPOIInfoResponseType


LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "src" / "python_ctrip" / "basedata" / "data"
COUNTRY_LIST_PATH = DATA_DIR / "country_list.json"

# Keep the historical default set.  Use --country or --all to select another set.
DEFAULT_COUNTRIES = (
    "中国",
    "加拿大",
    "德国",
    "意大利",
    "新加坡",
    "日本",
    "法国",
    "澳大利亚",
    "瑞士",
    "美国",
    "英国",
    "荷兰",
    "阿联酋",
    "韩国",
)


def load_country_list(path: Path = COUNTRY_LIST_PATH) -> list[dict[str, object]]:
    """Read the country metadata used to resolve country names to IDs."""
    with path.open("r", encoding="utf-8") as file:
        payload = json.load(file)
    countries = payload.get("countryList")
    if not isinstance(countries, list):
        raise ValueError(f"country list is missing from {path}")
    return [country for country in countries if isinstance(country, dict)]


def build_city_mapping(
    payload: QueryAllPOIInfoResponseType,
) -> dict[str, list[str]]:
    """Return each county/district name mapped to its parent city names."""
    result: dict[str, list[str]] = {}
    for province in payload.dataList or []:
        for city in province.prefectureLevelCityInfoList or []:
            city_name = city.cityName
            if not city_name:
                continue
            children: Iterable[str | None] = [
                *(county.countyName for county in city.countyList or []),
                *(district.districtName for district in city.districtList or []),
            ]
            for child_name in children:
                if not child_name:
                    continue
                parent_cities = result.setdefault(child_name, [])
                if city_name not in parent_cities:
                    parent_cities.append(city_name)
    return result


def write_city_mapping(path: Path, mapping: dict[str, list[str]]) -> None:
    """Write JSON atomically so an interrupted request cannot truncate a file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    with temporary_path.open("w", encoding="utf-8", newline="\n") as file:
        json.dump(mapping, file, ensure_ascii=False, indent=2)
        file.write("\n")
    temporary_path.replace(path)


def resolve_countries(
    country_list: list[dict[str, object]],
    names: Iterable[str],
) -> list[tuple[str, int]]:
    by_name = {
        country.get("name"): country.get("countryId")
        for country in country_list
        if isinstance(country.get("name"), str)
    }
    resolved: list[tuple[str, int]] = []
    for name in names:
        country_id = by_name.get(name)
        if not isinstance(country_id, int):
            raise ValueError(f"country {name!r} was not found in {COUNTRY_LIST_PATH}")
        resolved.append((name, country_id))
    return resolved


async def refresh(countries: Iterable[tuple[str, int]], output_dir: Path) -> None:
    client = BaseDataClient()
    for name, country_id in countries:
        LOGGER.info("Fetching %s (country_id=%s)", name, country_id)
        raw_response = await client.query_all_poi_info_raw(
            country_id=country_id,
            return_airport=False,
            return_bus_station=False,
            return_train_station=False,
        )
        payload = QueryAllPOIInfoResponseType.model_validate(raw_response)
        mapping = build_city_mapping(payload)
        output_path = output_dir / f"{name}.json"
        write_city_mapping(output_path, mapping)
        LOGGER.info("Wrote %s entries to %s", len(mapping), output_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--country",
        action="append",
        dest="countries",
        help="country name to refresh; may be repeated (default: historical set)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="refresh every country in country_list.json",
    )
    parser.add_argument(
        "--country-list",
        type=Path,
        default=COUNTRY_LIST_PATH,
        help=f"country metadata JSON (default: {COUNTRY_LIST_PATH})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DATA_DIR,
        help=f"directory for generated files (default: {DATA_DIR})",
    )
    parser.add_argument("--verbose", action="store_true", help="enable debug logging")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    load_dotenv()
    country_list = load_country_list(args.country_list)
    if args.all and args.countries:
        raise SystemExit("--all cannot be combined with --country")
    selected_names = (
        [str(country["name"]) for country in country_list]
        if args.all
        else args.countries or DEFAULT_COUNTRIES
    )
    countries = resolve_countries(country_list, selected_names)
    asyncio.run(refresh(countries, args.output_dir))


if __name__ == "__main__":
    main()
