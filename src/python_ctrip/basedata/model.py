from __future__ import annotations

from typing import Any, Optional

from ..ctrip_base_model import CtripBaseModel


class TicketRequest(CtripBaseModel):
    appKey: Optional[str] = None
    appSecurity: Optional[str] = None


class ResponseStatus(CtripBaseModel):
    success: Optional[bool] = None
    message: Optional[str] = None
    errorMessage: Optional[str] = None
    errorCode: Optional[int] = None


class TicketStatus(CtripBaseModel):
    Success: Optional[bool] = None
    Message: Optional[str] = None
    ErrorCode: Optional[int] = None


class TicketResponse(CtripBaseModel):
    Ticket: Optional[str] = None
    Status: Optional[TicketStatus] = None


class Authentification(CtripBaseModel):
    AppKey: Optional[str] = None
    Ticket: Optional[str] = None


class SearchRequest(CtripBaseModel):
    requestId: Optional[str] = None
    locale: Optional[str] = None
    auth: Optional[Authentification] = None


class CountryBaseInfo(CtripBaseModel):
    countryId: Optional[int] = None
    name: Optional[str] = None
    enName: Optional[str] = None
    code: Optional[str] = None
    continentId: Optional[int] = None
    continentName: Optional[str] = None


class FlightSearchResponse(CtripBaseModel):
    responseCode: Optional[int] = None
    responseDesc: Optional[str] = None
    countryList: Optional[list[CountryBaseInfo]] = None


class PrefectureLevelCityCondition(CtripBaseModel):
    prefectureLevelCityIds: Optional[str] = None
    prefectureLevelCityNames: Optional[str] = None
    returnDistrict: Optional[bool] = None
    returnCounty: Optional[bool] = None


class ProvinceCondition(CtripBaseModel):
    provinceIds: Optional[str] = None
    provinceNames: Optional[str] = None
    prefectureLevelCityConditions: Optional[PrefectureLevelCityCondition] = None


class POICondition(CtripBaseModel):
    returnAirport: Optional[bool] = None
    returnTrainStation: Optional[bool] = None
    returnBusStation: Optional[bool] = None


class QueryAllPOIInfoRequestType(CtripBaseModel):
    auth: Optional[Authentification] = None
    countryId: Optional[int] = None
    provinceConditions: Optional[ProvinceCondition] = None
    poiConditions: Optional[POICondition] = None
    startDate: Optional[str] = None


class AirportBuildingPOIInfo(CtripBaseModel):
    buildingId: Optional[int] = None
    buildingName: Optional[str] = None
    buildingEnName: Optional[str] = None
    shortName: Optional[str] = None
    shortNameEN: Optional[str] = None
    smsName: Optional[str] = None


class AirportPOIInfo(CtripBaseModel):
    airportCode: Optional[str] = None
    airportName: Optional[str] = None
    airportEnName: Optional[str] = None
    airportBuildingList: Optional[list[AirportBuildingPOIInfo]] = None
    airportTypeList: Optional[list[str]] = None


class TrainStationPOIInfo(CtripBaseModel):
    trainCode: Optional[str] = None
    trainName: Optional[str] = None
    trainEnName: Optional[str] = None


class BusStationPOIInfo(CtripBaseModel):
    busName: Optional[str] = None
    busPinYinName: Optional[str] = None


class StationInfo(CtripBaseModel):
    airportList: Optional[list[AirportPOIInfo]] = None
    trainStationList: Optional[list[TrainStationPOIInfo]] = None
    busStationList: Optional[list[BusStationPOIInfo]] = None


class CountyLevelCityPOI(CtripBaseModel):
    countyId: Optional[int] = None
    countyName: Optional[str] = None
    countyEnName: Optional[str] = None
    corpTag: Optional[int] = None
    stationInfo: Optional[StationInfo] = None
    countyCode: Optional[str] = None
    countyPinyin: Optional[str] = None
    districtCode: Optional[str] = None


class DistrictPOIInfo(CtripBaseModel):
    districtId: Optional[int] = None
    districtName: Optional[str] = None
    districtEnName: Optional[str] = None
    districtCode: Optional[str] = None


class PrefectureLevelCityInfo(CtripBaseModel):
    cityId: Optional[int] = None
    cityName: Optional[str] = None
    cityEnName: Optional[str] = None
    corpTag: Optional[int] = None
    stationInfo: Optional[StationInfo] = None
    countyList: Optional[list[CountyLevelCityPOI]] = None
    districtList: Optional[list[DistrictPOIInfo]] = None
    districtCode: Optional[str] = None
    cityCode: Optional[str] = None
    cityPinYin: Optional[str] = None


class POIData(CtripBaseModel):
    provinceId: Optional[int] = None
    provinceName: Optional[str] = None
    provinceEnName: Optional[str] = None
    prefectureLevelCityInfoList: Optional[list[PrefectureLevelCityInfo]] = None


class InvalidGeoInfo(CtripBaseModel):
    geoId: Optional[int] = None
    geoCategoryId: Optional[int] = None


class QueryAllPOIInfoResponseType(CtripBaseModel):
    responseStatus: Optional["GatewayResponseStatus"] = None
    status: Optional[ResponseStatus] = None
    dataList: Optional[list[POIData]] = None
    invalidGeoList: Optional[list[InvalidGeoInfo]] = None


class GatewayResponseStatus(CtripBaseModel):
    timestamp: Optional[str] = None
    ack: Optional[str] = None
    errors: Optional[list[Any]] = None


class Country(CtripBaseModel):
    countryId: Optional[int] = None
    name: Optional[str] = None
    enName: Optional[str] = None
    code: Optional[str] = None
    continentId: Optional[int] = None
    continentName: Optional[str] = None
    areaCode: Optional[str] = None


__all__ = [
    "AirportBuildingPOIInfo",
    "AirportPOIInfo",
    "Authentification",
    "BusStationPOIInfo",
    "CtripBaseModel",
    "Country",
    "CountryBaseInfo",
    "CountyLevelCityPOI",
    "DistrictPOIInfo",
    "FlightSearchResponse",
    "GatewayResponseStatus",
    "InvalidGeoInfo",
    "POICondition",
    "POIData",
    "PrefectureLevelCityCondition",
    "PrefectureLevelCityInfo",
    "ProvinceCondition",
    "QueryAllPOIInfoRequestType",
    "QueryAllPOIInfoResponseType",
    "ResponseStatus",
    "SearchRequest",
    "StationInfo",
    "TicketRequest",
    "TicketResponse",
    "TrainStationPOIInfo",
]
