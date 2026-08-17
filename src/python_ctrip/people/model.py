from __future__ import annotations

from typing import Optional

from ..ctrip_base_model import CtripBaseModel


class CostCenterEntity(CtripBaseModel):
    CostCenterType: Optional[str] = None
    CostCenterContent: Optional[str] = None
    CostCenterContentEN: Optional[str] = None
    IsDefault: Optional[bool] = None


class ConfirmPersonEntity(CtripBaseModel):
    ProductType: Optional[str] = None
    AuthorizedTime: Optional[int] = None
    ConfirmPerson: Optional[str] = None
    ConfirmPersoncc: Optional[str] = None
    IsDefault: Optional[bool] = None


class UserCardInfoEntity(CtripBaseModel):
    CardNo: Optional[str] = None
    CardType: Optional[int] = None
    IDCardTimelimit: Optional[str] = None
    PassportType: Optional[str] = None
    Assigned: Optional[str] = None


class UserFFPInfoEntity(CtripBaseModel):
    Airline: Optional[str] = None
    FFPNo: Optional[str] = None


class CorpEmailSendRuleEntity(CtripBaseModel):
    EmailSendNode: Optional[str] = None
    ReceiverEMail: Optional[str] = None
    EmailSendRuleLanguage: Optional[str] = None
    IsSendCardHolder: Optional[str] = None
    IsSendContactor: Optional[str] = None
    BusinessType: Optional[int] = None
    EmailSendRuleValid: Optional[str] = None
    IsRefundPassenger: Optional[str] = None
    IsChangePassenger: Optional[str] = None
    ReceiverPhone: Optional[str] = None
    SendType: Optional[str] = None
    ReceiverEmployeeID: Optional[str] = None
    IsSendApprover: Optional[str] = None
    IsSendPassenger: Optional[str] = None


class CorpTicketReservationEntity(CtripBaseModel):
    ResUid: Optional[str] = None
    ResEid: Optional[str] = None
    ResValid: Optional[str] = None


class UserGroupInfoEntity(CtripBaseModel):
    GroupID: Optional[int] = None
    Valid: Optional[str] = None


class AuthencationEntity(CtripBaseModel):
    EmployeeID: Optional[str] = None
    Name: Optional[str] = None
    NameENFirstName: Optional[str] = None
    NameENMiddleName: Optional[str] = None
    NameENLastName: Optional[str] = None
    Nationality: Optional[str] = None
    Gender: Optional[str] = None
    Birthday: Optional[str] = None
    NickName: Optional[str] = None
    MobilePhone: Optional[str] = None
    CountryCode: Optional[int] = None
    Email: Optional[str] = None
    Address: Optional[str] = None
    PostCode: Optional[str] = None
    ContactTel: Optional[str] = None
    ContactFax: Optional[str] = None
    UserCardInfos: Optional[list[UserCardInfoEntity]] = None
    UserFFPInfos: Optional[list[UserFFPInfoEntity]] = None
    DockingVendorPlatform: Optional[int] = None
    DockingVendorPlatformAccount: Optional[str] = None
    NoticeLanguage: Optional[str] = None
    Valid: Optional[str] = None
    RankName: Optional[str] = None
    WorkCity: Optional[str] = None
    WorkCityID: Optional[int] = None
    Dept1: Optional[str] = None
    Dept2: Optional[str] = None
    Dept3: Optional[str] = None
    Dept4: Optional[str] = None
    Dept5: Optional[str] = None
    Dept6: Optional[str] = None
    Dept7: Optional[str] = None
    Dept8: Optional[str] = None
    Dept9: Optional[str] = None
    Dept10: Optional[str] = None
    CostCenter: Optional[str] = None
    CostCenter2: Optional[str] = None
    CostCenter3: Optional[str] = None
    CostCenter1EN: Optional[str] = None
    CostCenter2EN: Optional[str] = None
    CostCenter3EN: Optional[str] = None
    IsCostCenter1Optional: Optional[bool] = None
    IsCostCenter2Optional: Optional[bool] = None
    IsCostCenter3Optional: Optional[bool] = None
    CostCenterList: Optional[list[CostCenterEntity]] = None
    SubAccountName: Optional[str] = None
    CorpCardType: Optional[str] = None
    ResRange: Optional[str] = None
    IsAuthorizedOptional: Optional[bool] = None
    ConfirmPersonList: Optional[list[ConfirmPersonEntity]] = None
    AuthPWD: Optional[str] = None
    IsAutoGenerateAuthPWD: Optional[bool] = None
    IsAuthPWDSetUpSendRemind: Optional[bool] = None
    AuthPWDEmailLanguage: Optional[str] = None
    IsBookClass: Optional[str] = None
    IntlBookClassBlock: Optional[str] = None
    IsSendEMail: Optional[bool] = None
    IsSendSms: Optional[bool] = None
    AuthEmailLanguage: Optional[str] = None
    ConcurAccount: Optional[str] = None
    CorpEmailSendRules: Optional[list[CorpEmailSendRuleEntity]] = None
    CorpTicketReservations: Optional[list[CorpTicketReservationEntity]] = None
    UseTRFlag: Optional[int] = None
    FltClassStandard: Optional[str] = None
    FltRateStandard: Optional[float] = None
    SuperiorEID: Optional[str] = None
    SuperiorEmail: Optional[str] = None
    SuperiorMobile: Optional[str] = None
    SuperiorName: Optional[str] = None
    SuperiorEmailLanguage: Optional[str] = None
    CustID: Optional[str] = None
    IsServedCard: Optional[str] = None
    CanBookTrainSeat: Optional[str] = None
    IsTrainOtherSeatCanBook: Optional[str] = None
    ReservationFlightHD: Optional[int] = None
    FlightHighRateAirline: Optional[str] = None
    RefundAuth: Optional[int] = None
    IsShieldCabinN: Optional[str] = None
    DomesticTicketType: Optional[str] = None
    IntlTicketType: Optional[str] = None
    DomesticTicketSendAddressID: Optional[int] = None
    IntlTicketSendAddressID: Optional[int] = None
    CivilServantPrice: Optional[int] = None
    UserGroupInfoList: Optional[list[UserGroupInfoEntity]] = None
    Mice: Optional[str] = None


AuthenticationEntity = AuthencationEntity


class AuthenticationInfo(CtripBaseModel):
    Sequence: Optional[str] = None
    Authentication: Optional[AuthencationEntity] = None


class AuthenticationListRequest(CtripBaseModel):
    Language: Optional[str] = None
    Appkey: Optional[str] = None
    Ticket: Optional[str] = None
    CorporationID: Optional[str] = None
    AuthenticationInfoList: Optional[list[AuthenticationInfo]] = None


class ErrorMessage(CtripBaseModel):
    Sequence: Optional[int] = None
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None
    EmployeeID: Optional[str] = None


class AuthenticationResponseList(CtripBaseModel):
    Result: Optional[str] = None
    ErrorMessageList: Optional[list[ErrorMessage]] = None


class TicketRequest(CtripBaseModel):
    appKey: Optional[str] = None
    appSecurity: Optional[str] = None


class ResponseStatus(CtripBaseModel):
    Success: Optional[bool] = None
    Message: Optional[str] = None
    ErrorCode: Optional[int] = None


class TicketResponse(CtripBaseModel):
    Ticket: Optional[str] = None
    Status: Optional[ResponseStatus] = None


__all__ = [
    "AuthenticationEntity",
    "AuthenticationInfo",
    "AuthenticationListRequest",
    "AuthenticationResponseList",
    "AuthencationEntity",
    "CtripBaseModel",
    "ConfirmPersonEntity",
    "CorpEmailSendRuleEntity",
    "CorpTicketReservationEntity",
    "CostCenterEntity",
    "ErrorMessage",
    "ResponseStatus",
    "TicketRequest",
    "TicketResponse",
    "UserCardInfoEntity",
    "UserFFPInfoEntity",
    "UserGroupInfoEntity",
]
