from __future__ import annotations

from typing import Optional

from ..ctrip_base_model import CtripBaseModel




class ResponseStatus(CtripBaseModel):
    Success: Optional[bool] = None
    Message: Optional[str] = None
    ErrorCode: Optional[int] = None


class TicketRequest(CtripBaseModel):
    appKey: Optional[str] = None
    appSecurity: Optional[str] = None


class TicketResponse(CtripBaseModel):
    Ticket: Optional[str] = None
    Status: Optional[ResponseStatus] = None


class Authentification(CtripBaseModel):
    AppKey: Optional[str] = None
    Ticket: Optional[str] = None


class ExtendField(CtripBaseModel):
    FieldName: Optional[str] = None
    FieldValue: Optional[str] = None
    FieldType: Optional[str] = None


class RankInfo(CtripBaseModel):
    RankName: Optional[str] = None


class PassengerDetail(CtripBaseModel):
    Name: Optional[str] = None
    CredentialsType: Optional[str] = None
    CredentialsNumber: Optional[str] = None
    EID: Optional[str] = None
    NameEn: Optional[str] = None
    LastName: Optional[str] = None
    FirstName: Optional[str] = None
    RankName: Optional[str] = None
    PolicyEID: Optional[str] = None
    countryCode: Optional[str] = None
    mobilePhone: Optional[str] = None
    ExtendFieldList: Optional[list[ExtendField]] = None
    AveragePrice: Optional[str] = None


class TripSegment(CtripBaseModel):
    SectorIndex: Optional[int] = None
    DepartCityId: Optional[str] = None
    ArrivalCityId: Optional[str] = None
    DepartBeginDate: Optional[str] = None
    DepartEndDate: Optional[str] = None
    DefaultDepartDate: Optional[str] = None


class FlightEndorsementDetail(CtripBaseModel):
    BookingTypeList: Optional[list[str]] = None
    OrderIDList: Optional[list[str]] = None
    Airline: Optional[str] = None
    Currency: Optional[str] = None
    FlightWay: Optional[int] = None
    ChangeFlightWay: Optional[bool] = None
    DepartDateBegin: Optional[str] = None
    DepartDateEnd: Optional[str] = None
    ReturnDateBegin: Optional[str] = None
    ReturnDateEnd: Optional[str] = None
    TakeOffBeginTime: Optional[str] = None
    TakeOffEndTime: Optional[str] = None
    ArrivalBeginTime: Optional[str] = None
    ArrivalEndTime: Optional[str] = None
    Discount: Optional[float] = None
    DepartCountryIds: Optional[list[str]] = None
    DepartCountryCodes: Optional[list[str]] = None
    DepartCityCodes: Optional[list[str]] = None
    ArrivalCountryIds: Optional[list[str]] = None
    ArrivalCountryCodes: Optional[list[str]] = None
    ArrivalCityCodes: Optional[list[str]] = None
    DepartCityIds: Optional[list[str]] = None
    ArrivalCityIds: Optional[list[str]] = None
    PassengerList: Optional[list[PassengerDetail]] = None
    Price: Optional[float] = None
    ProductType: Optional[str] = None
    SeatClass: Optional[int] = None
    SkipFields: Optional[int] = None
    TravelerCount: Optional[int] = None
    TotalTravelerCount: Optional[int] = None
    PreVerifyFields: Optional[int] = None
    RankInfo: Optional[RankInfo] = None
    TripSegmentCheckPolicy: Optional[str] = None
    TripSegmentList: Optional[list[TripSegment]] = None


class HotelEndorsementDetail(CtripBaseModel):
    ProductType: Optional[str] = None
    CheckInDateBegin: Optional[str] = None
    CheckInDateEnd: Optional[str] = None
    CheckOutDateBegin: Optional[str] = None
    CheckOutDateEnd: Optional[str] = None
    PassengerList: Optional[list[PassengerDetail]] = None
    CheckInCountryIds: Optional[list[str]] = None
    CheckInCountryCodes: Optional[list[str]] = None
    CheckInCityCodes: Optional[list[str]] = None
    CheckInLocationIdList: Optional[list[str]] = None
    MaxPrice: Optional[str] = None
    MinPrice: Optional[str] = None
    Currency: Optional[str] = None
    MaxStarRating: Optional[str] = None
    MinStarRating: Optional[str] = None
    AveragePrice: Optional[str] = None
    RoomCount: Optional[int] = None
    SkipFields: Optional[int] = None
    TotalRoomNightCount: Optional[int] = None
    RoomNightPrice: Optional[str] = None
    PreVerifyFields: Optional[int] = None
    RankInfo: Optional[RankInfo] = None


class TrainEndorsementDetail(CtripBaseModel):
    ProductType: Optional[str] = None
    BookingTypeList: Optional[list[str]] = None
    OrderIDList: Optional[list[str]] = None
    TripType: Optional[int] = None
    DepartDateBegin: Optional[str] = None
    DepartDateEnd: Optional[str] = None
    ReturnDateBegin: Optional[str] = None
    ReturnDateEnd: Optional[str] = None
    PassengerList: Optional[list[PassengerDetail]] = None
    ArrivalCityCodes: Optional[list[str]] = None
    DepartCityCodes: Optional[list[str]] = None
    Price: Optional[str] = None
    Currency: Optional[str] = None
    SeatType: Optional[list[str]] = None
    SkipFields: Optional[int] = None
    TravelerCount: Optional[int] = None
    PreVerifyFields: Optional[int] = None
    subSeatTypeIDList: Optional[list[str]] = None
    trainVehicleTypeList: Optional[list[str]] = None
    TotalTravelerCount: Optional[int] = None
    RankInfo: Optional[RankInfo] = None


class CompanyAddressDetail(CtripBaseModel):
    CoordinateType: Optional[str] = None
    AddressName: Optional[str] = None
    Longitude: Optional[str] = None
    Latitude: Optional[str] = None
    AllowRadius: Optional[int] = None


class UseTimeDetail(CtripBaseModel):
    BeginUseTime: Optional[str] = None
    EndUseTime: Optional[str] = None


class CarQuickEndorsementDetail(CtripBaseModel):
    ProductType: Optional[int] = None
    PassengerList: Optional[list[PassengerDetail]] = None
    Cities: Optional[str] = None
    ArrivalCities: Optional[str] = None
    CompanyAddressList: Optional[list[CompanyAddressDetail]] = None
    ArrivalAddressList: Optional[list[CompanyAddressDetail]] = None
    BeginUseDate: Optional[str] = None
    EndUseDate: Optional[str] = None
    UseTimeList: Optional[list[UseTimeDetail]] = None
    Currency: Optional[str] = None
    Price: Optional[float] = None
    VehicleGroup: Optional[str] = None
    EffectivenessAmount: Optional[int] = None
    SkipFields: Optional[int] = None
    CarScene: Optional[int] = None
    RankInfo: Optional[RankInfo] = None


class SaveApprovalRequest(CtripBaseModel):
    ApprovalNumber: Optional[str] = None
    Status: Optional[int] = None
    CtripCardNO: Optional[str] = None
    EmployeeID: Optional[str] = None
    FlightEndorsementDetails: Optional[list[FlightEndorsementDetail]] = None
    HotelEndorsementDetails: Optional[list[HotelEndorsementDetail]] = None
    TrainEndorsementDetails: Optional[list[TrainEndorsementDetail]] = None
    CarQuickEndorsementDetails: Optional[list[CarQuickEndorsementDetail]] = None
    ExpiredTime: Optional[str] = None
    Auth: Optional[Authentification] = None
    ExtendFieldList: Optional[list[ExtendField]] = None
    Remark: Optional[str] = None
    RankInfo: Optional[RankInfo] = None





class SetApprovalResultStatus(CtripBaseModel):
    Status: Optional[ResponseStatus] = None
    approvalNumber: Optional[str] = None

class SetApprovalResult(CtripBaseModel):
    SetApprovalResult: Optional[SetApprovalResultStatus] = None


__all__ = [
    "Authentification",
    "CarQuickEndorsementDetail",
    "CompanyAddressDetail",
    "ExtendField",
    "FlightEndorsementDetail",
    "HotelEndorsementDetail",
    "PassengerDetail",
    "RankInfo",
    "ResponseStatus",
    "SaveApprovalRequest",
    "SetApprovalResult",
    "TicketRequest",
    "TicketResponse",
    "TrainEndorsementDetail",
    "TripSegment",
    "UseTimeDetail",
]
