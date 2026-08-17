from __future__ import annotations

from decimal import Decimal
from typing import Optional

from pydantic import Field

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


class FlightOrderSettlementQueryRequest(CtripBaseModel):
    Auth: Optional[Authentification] = None
    AccountID: Optional[str] = None
    DateFrom: Optional[str] = None
    DateTo: Optional[str] = None
    BatchNo: Optional[str] = None
    RecordID: Optional[str] = None
    OrderID: Optional[int] = None
    JourneyNoList: Optional[list[str]] = None
    IsCompensation: Optional[bool] = None
    PayType: Optional[str] = None
    PageIndex: Optional[int] = None
    PageSize: Optional[int] = None
    SubBatchNoList: Optional[list[str]] = None
    preApprovalNoList: Optional[list[str]] = None


class FeeDetail(CtripBaseModel):
    CombineDetailId: Optional[int] = None
    FeeCode: Optional[str] = None
    FeeAmount: Optional[Decimal] = None


class StandardGeoEntity(CtripBaseModel):
    countryId: Optional[int] = None
    countryName: Optional[str] = None
    countryEnName: Optional[str] = None
    provinceId: Optional[int] = None
    provinceName: Optional[str] = None
    provinceEnName: Optional[str] = None
    cityId: Optional[int] = None
    cityName: Optional[str] = None
    cityEnName: Optional[str] = None
    districtId: Optional[int] = None
    districtName: Optional[str] = None
    districtEnName: Optional[str] = None
    countryCode: Optional[str] = None


class StandardGeoInfo(CtripBaseModel):
    DepartureInfo: Optional[StandardGeoEntity] = None
    ArrivalInfo: Optional[StandardGeoEntity] = None


class FlightOrderSettlementBaseInfo(CtripBaseModel):
    RecordID: Optional[int] = None
    OrderID: Optional[int] = None
    Sequence: Optional[int] = None
    CreateTime: Optional[str] = None
    AccountID: Optional[int] = None
    CorpID: Optional[str] = None
    AccCheckBatchNo: Optional[str] = None
    AccBalanceBatchNo: Optional[str] = None
    SubAccCheckBatchNo: Optional[str] = None
    OrderDetailType: Optional[str] = None
    OrderType: Optional[int] = None
    SettlementCurrency: Optional[str] = None
    InvoiceIds: Optional[list[int]] = None
    FeeDetailKvList: Optional[list[FeeDetail]] = None
    IsChecked: Optional[bool] = None
    PayMixFlag: Optional[bool] = None
    RealPaymentType: Optional[str] = None
    BatchStartDate: Optional[str] = None
    BatchEndDate: Optional[str] = None
    TripID: Optional[int] = None
    Price: Optional[Decimal] = None
    Tax: Optional[Decimal] = None
    OilFee: Optional[Decimal] = None
    Amount: Optional[Decimal] = None
    TotalAmount: Optional[Decimal] = None
    AccountPayAmount: Optional[Decimal] = None
    PersonalPayAmount: Optional[Decimal] = None
    PersonalPayAmountSummary: Optional[Decimal] = None
    PostServiceFee: Optional[Decimal] = None
    ServiceFee: Optional[Decimal] = None
    Refund: Optional[Decimal] = None
    RebookQueryFee: Optional[Decimal] = None
    PriceDifferential: Optional[Decimal] = None
    DateChangeFee: Optional[Decimal] = None
    OilFeeDifferential: Optional[Decimal] = None
    TaxFeeDifferential: Optional[Decimal] = None
    DeductibleTax: Optional[Decimal] = None
    NonDeductibleTax: Optional[Decimal] = None
    RealAmountWithPostServiceFee: Optional[Decimal] = None


class FlightOrderBaseInfo(CtripBaseModel):
    Uid: Optional[str] = None
    Rank: Optional[str] = None
    EmployeeID: Optional[str] = None
    Name: Optional[str] = None
    CtripCardNo: Optional[str] = None
    JourneyID: Optional[str] = None
    OrderStatus: Optional[str] = None
    OrderDate: Optional[str] = None
    PrintTicketTime: Optional[str] = None
    ProductType: Optional[str] = None
    FlightClass: Optional[str] = None
    Project: Optional[str] = None
    ProjectCode: Optional[str] = None
    PrepayType: Optional[str] = None
    ReservationType: Optional[str] = None
    PreEmail: Optional[str] = None
    PrepareApprovalStatus: Optional[int] = None
    ShoppingEnum: Optional[str] = None
    ProvideBillType: Optional[str] = None
    AgreementType: Optional[str] = None
    CostCenter: Optional[str] = None
    CostCenter2: Optional[str] = None
    CostCenter3: Optional[str] = None
    CostCenter4: Optional[str] = None
    CostCenter5: Optional[str] = None
    CostCenter6: Optional[str] = None
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


class FlightOrderPassenger(CtripBaseModel):
    Sequence: Optional[int] = None
    PassengerName: Optional[str] = None
    TicketNo: Optional[str] = None
    TicketNoSignCode: Optional[str] = None
    CardTypeName: Optional[str] = None
    CardTypeNumber: Optional[str] = None
    EmployeeID: Optional[str] = None
    PassengerEmail: Optional[str] = None
    PassengerNamePY: Optional[str] = None
    PassengerPreApprovalNo: Optional[str] = None
    BookApprovalStatus: Optional[int] = None
    FinanceStatus: Optional[int] = None


class FlightOrderRebookInfo(CtripBaseModel):
    Sequence: Optional[int] = None
    PassengerName: Optional[str] = None
    RebookingTime: Optional[str] = None
    RebookedTime: Optional[str] = None
    ExchangeFlight: Optional[str] = None
    TicketNo: Optional[str] = None
    TicketNOWithAC: Optional[str] = None
    RebookApprovalNo: Optional[str] = None
    PreApprovalStatus: Optional[int] = None
    Rid: Optional[int] = None
    standard_geo_info: Optional[StandardGeoInfo] = Field(default=None, alias="StandardGeoInfo")
    PriceRate: Optional[Decimal] = None
    OilFeeDifferential: Optional[Decimal] = None
    ControlCabinClass: Optional[str] = None


class FlightOrderRefundInfo(CtripBaseModel):
    Sequence: Optional[int] = None
    PassengerName: Optional[str] = None
    RefundTime: Optional[str] = None
    Flight: Optional[str] = None
    TicketNo: Optional[str] = None
    TicketNOWithAC: Optional[str] = None
    RefundApprovalId: Optional[str] = None
    TotalEmdAmount: Optional[Decimal] = None


class OrderFlightInfo(CtripBaseModel):
    Sequence: Optional[int] = None
    Flight: Optional[str] = None
    TakeOffTime: Optional[str] = None
    ArrivalTime: Optional[str] = None
    TakeOffTimeUTC: Optional[str] = None
    ArrivalTimeUTC: Optional[str] = None
    DCityName: Optional[str] = None
    ACityName: Optional[str] = None
    DPortName: Optional[str] = None
    APortName: Optional[str] = None
    Class: Optional[str] = None
    ClassName: Optional[str] = None
    SubClass: Optional[str] = None
    StandardPrice: Optional[Decimal] = None
    PriceRate: Optional[Decimal] = None
    standard_geo_info: Optional[StandardGeoInfo] = Field(default=None, alias="StandardGeoInfo")
    ControlCabinClass: Optional[str] = None
    flightType: Optional[str] = None
    vehicleType: Optional[str] = None
    flightWay: Optional[str] = None


class FlightOrderSegmentPrintInfo(CtripBaseModel):
    OrderID: Optional[int] = None
    itineraryType: Optional[str] = None
    printDetailStatus: Optional[str] = None
    ExpressNo: Optional[str] = None
    PassengerName: Optional[str] = None
    TicketNo: Optional[str] = None
    RealTicketNo: Optional[str] = None
    PrintNo: Optional[str] = None
    SegmentPrintPrice: Optional[Decimal] = None
    PrintTime: Optional[int] = None
    AirLineCode: Optional[str] = None
    OrderStatus: Optional[str] = None
    valueAddTax: Optional[Decimal] = None
    TicketNoSignCode: Optional[str] = None


class FlightOrderExpressInfo(CtripBaseModel):
    ExpressID: Optional[str] = None


class FlightOrderPrintDetailInfo(CtripBaseModel):
    OrderID: Optional[int] = None
    CorpID: Optional[str] = None
    FlightOrderSegmentPrintInfoList: Optional[list[FlightOrderSegmentPrintInfo]] = None
    RegularExpressInfoListFieldList: Optional[list[FlightOrderExpressInfo]] = None


class ApprovalLevelInfo(CtripBaseModel):
    level: Optional[int] = None
    accreditors: Optional[list[str]] = None


class ApprovalFlowInfo(CtripBaseModel):
    ApprovalLevelList: Optional[list[ApprovalLevelInfo]] = None


class FlightOrderSettlementInfo(CtripBaseModel):
    OrderSettlementBaseInfo: Optional[FlightOrderSettlementBaseInfo] = None
    OrderBaseInfo: Optional[FlightOrderBaseInfo] = None
    OrderPassengerInfo: Optional[FlightOrderPassenger] = None
    OrderRebookInfo: Optional[FlightOrderRebookInfo] = None
    OrderRefundInfo: Optional[FlightOrderRefundInfo] = None
    order_flight_info: Optional[OrderFlightInfo] = Field(default=None, alias="OrderFlightInfo")
    OrderPrintDetailInfo: Optional[FlightOrderPrintDetailInfo] = None
    approval_flow_info: Optional[ApprovalFlowInfo] = Field(default=None, alias="ApprovalFlowInfo")


class FlightOrderAccountSettlementInfo(CtripBaseModel):
    AccountID: Optional[int] = None
    OrderSettlementList: Optional[list[FlightOrderSettlementInfo]] = None


class FlightOrderSettlementQueryResponse(CtripBaseModel):
    FlightOrderAccountSettlementList: Optional[list[FlightOrderAccountSettlementInfo]] = None
    Status: Optional[ResponseStatus] = None
    TotalRecord: Optional[int] = None
    TotalSize: Optional[int] = None


class HotelOrderDetailQueryRequest(CtripBaseModel):
    Auth: Optional[Authentification] = None
    AccountId: Optional[str] = None
    DateFrom: Optional[str] = None
    DateTo: Optional[str] = None
    HotelType: Optional[str] = None
    PayType: Optional[str] = None
    BatchNo: Optional[str] = None
    RecordId: Optional[str] = None
    OrderId: Optional[int] = None
    JourneyNoList: Optional[list[str]] = None
    IsCompensation: Optional[bool] = None
    PageIndex: Optional[int] = None
    PageSize: Optional[int] = None
    SubBatchNoList: Optional[list[str]] = None
    PreApprovalNoList: Optional[list[str]] = None


class DailyAvgPrice(CtripBaseModel):
    effectDate: Optional[str] = None
    averagePrice: Optional[Decimal] = None


class RefundDate(CtripBaseModel):
    RefundStartDate: Optional[str] = None
    RefundEndDate: Optional[str] = None


class HotelFeeDetail(CtripBaseModel):
    CombineDetailId: Optional[int] = None
    FeeCode: Optional[str] = None
    FeeAmount: Optional[Decimal] = None


class HotelSettlementDetail(CtripBaseModel):
    RecordId: Optional[int] = None
    OrderID: Optional[int] = None
    AccountId: Optional[int] = None
    Uid: Optional[str] = None
    DetailType: Optional[str] = None
    PayType: Optional[str] = None
    HotelType: Optional[str] = None
    Price: Optional[Decimal] = None
    Quantity: Optional[int] = None
    Amount: Optional[Decimal] = None
    Servicefee: Optional[Decimal] = None
    ExtraCharge: Optional[Decimal] = None
    AccCheckBatchNo: Optional[str] = None
    Createtime: Optional[str] = None
    Datachange_Lasttime: Optional[str] = None
    OrderType: Optional[int] = None
    SubAccCheckBatchNo: Optional[str] = None
    TripID: Optional[int] = None
    SettlementCurrency: Optional[str] = None
    IsChecked: Optional[bool] = None
    DailyAvgPriceInfo: Optional[list[DailyAvgPrice]] = None
    InvoiceIds: Optional[list[int]] = None
    BatchStartDate: Optional[str] = None
    BatchEndDate: Optional[str] = None
    FrontendServiceFee: Optional[Decimal] = None
    Coupon: Optional[Decimal] = None
    RelatedCostsID: Optional[int] = None
    ApportionMode: Optional[str] = None
    OrderRoomMode: Optional[str] = None
    ClientApprovalNo: Optional[str] = None
    FellowApprovalNo: Optional[str] = None
    LoanServiceFee: Optional[Decimal] = None
    ClientName: Optional[str] = None
    EmployeeID: Optional[str] = None
    InsuranceAmount: Optional[Decimal] = None
    PersonAmount: Optional[Decimal] = None
    ChannelFee: Optional[Decimal] = None
    PersonalChannelFee: Optional[Decimal] = None
    PaidAmount: Optional[Decimal] = None
    PersonalTotalAmount: Optional[Decimal] = None
    PersonalRemittedTax: Optional[Decimal] = None
    BookServiceFee: Optional[Decimal] = None
    ModifyServiceFee: Optional[Decimal] = None
    CancelServiceFee: Optional[Decimal] = None
    PayDiscountAmount: Optional[Decimal] = None
    AverageRoomPrice: Optional[Decimal] = None
    UseCowrie: Optional[str] = None
    FeeDetailKvList: Optional[list[HotelFeeDetail]] = None
    TotalAmount: Optional[Decimal] = None
    AccountPayAmount: Optional[Decimal] = None
    PersonalPayAmount: Optional[Decimal] = None
    Deposit: Optional[Decimal] = None
    RemittedTaxType: Optional[str] = None
    RemittedTax: Optional[Decimal] = None
    LocalCurrencyAmount: Optional[Decimal] = None
    RefundDateList: Optional[list[RefundDate]] = None
    PaymentType: Optional[str] = None


class HotelSettlementClientDetail(CtripBaseModel):
    EmployeeID: Optional[str] = None
    ClientName: Optional[str] = None
    CostCenter1: Optional[str] = None
    CostCenter2: Optional[str] = None
    CostCenter3: Optional[str] = None
    CostCenter4: Optional[str] = None
    CostCenter5: Optional[str] = None
    CostCenter6: Optional[str] = None
    CostCenter7: Optional[str] = None
    CostCenter8: Optional[str] = None
    CostCenter9: Optional[str] = None
    CostCenter10: Optional[str] = None
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
    Checkin_Time: Optional[str] = None
    Checkout_Time: Optional[str] = None
    RoomIndex: Optional[int] = None
    ShareOrderAmount: Optional[Decimal] = None
    Maxprice: Optional[Decimal] = None
    ArrivalTime: Optional[str] = None
    DepartureTime: Optional[str] = None
    UserNamePinyin: Optional[str] = None
    ClientPreApprovalNo: Optional[str] = None
    ShareRoomStandard: Optional[bool] = None
    PassengerEmail: Optional[str] = None
    MobilePhone: Optional[str] = None
    BookApprovalStatus: Optional[int] = None
    JounaryNo: Optional[str] = None
    Project: Optional[str] = None
    ProjectCode: Optional[str] = None
    JounaryReason: Optional[str] = None
    DefineFlag1: Optional[str] = None
    DefineFlag2: Optional[str] = None


class HotelOrderDetail(CtripBaseModel):
    OrderId: Optional[int] = None
    EmployeeName: Optional[str] = None
    EmployeeID: Optional[str] = None
    WorkCity: Optional[str] = None
    OrderDate: Optional[str] = None
    RoomName: Optional[str] = None
    RoomNameEN: Optional[str] = None
    RoomQuantity: Optional[int] = None
    ClientName: Optional[str] = None
    StartTime: Optional[str] = None
    EndTime: Optional[str] = None
    PostAmount: Optional[Decimal] = None
    IsHasSpecialInvoice: Optional[str] = None
    ServerFrom: Optional[str] = None
    LowPriceRC: Optional[str] = None
    LowPriceRC_VV: Optional[str] = None
    LowPriceRCInfo: Optional[str] = None
    LowPriceRCInfoEN: Optional[str] = None
    AgreementRC: Optional[str] = None
    AgreementRC_VV: Optional[str] = None
    AgreementRCInfo: Optional[str] = None
    AgreementRCInfoEN: Optional[str] = None
    CostCenter: Optional[str] = None
    CostCenter2: Optional[str] = None
    CostCenter3: Optional[str] = None
    CostCenter4: Optional[str] = None
    CostCenter5: Optional[str] = None
    CostCenter6: Optional[str] = None
    JourneyReason: Optional[str] = None
    Project: Optional[str] = None
    DefineTitleContent: Optional[str] = None
    DefineTitleContent2: Optional[str] = None
    HotelRelatedJourneyNo: Optional[str] = None
    Remarks: Optional[str] = None
    PayType: Optional[str] = None
    BalanceType: Optional[str] = None
    IsMixPayment: Optional[str] = None
    SettlementACCNTAmt: Optional[Decimal] = None
    SettlementPersonAmt: Optional[Decimal] = None
    CouponAmount: Optional[Decimal] = None
    ClientDetailList: Optional[list[HotelSettlementClientDetail]] = None
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
    ProjectCode: Optional[str] = None
    CancelReason: Optional[str] = None
    CancelReasonDesc: Optional[str] = None
    RefundTime: Optional[str] = None
    UserNamePinyin: Optional[str] = None
    ReservationType: Optional[str] = None
    PreEmail: Optional[str] = None
    PrepareApprovalStatus: Optional[int] = None
    OrderStatus: Optional[str] = None


class SettlementHotelDetail(CtripBaseModel):
    HotelName: Optional[str] = None
    HotelNameEN: Optional[str] = None
    CityName: Optional[str] = None
    CityNameEN: Optional[str] = None
    Star: Optional[int] = None
    IsDomestic: Optional[bool] = None
    ISCU: Optional[str] = None
    CityID: Optional[int] = None
    DistrictCode: Optional[str] = None
    DistrictID: Optional[int] = None
    DistrictName: Optional[str] = None
    BrandName: Optional[str] = None
    standard_geo_info: Optional[StandardGeoEntity] = Field(default=None, alias="StandardGeoInfo")
    ParentCityID: Optional[int] = None
    ParentCityName: Optional[str] = None
    ParentCityEnName: Optional[str] = None
    HotelGroupId: Optional[int] = None
    HotelGroupName: Optional[str] = None


class HotelSettlementInfo(CtripBaseModel):
    SettlementDetail: Optional[HotelSettlementDetail] = None
    OrderDetail: Optional[HotelOrderDetail] = None
    HotelDetail: Optional[SettlementHotelDetail] = None
    approval_flow_info: Optional[ApprovalFlowInfo] = Field(default=None, alias="ApprovalFlowInfo")


class HotelAccountSettlementInfo(CtripBaseModel):
    AccountId: Optional[str | int] = None
    LstHotelSettlementDetail: Optional[list[HotelSettlementInfo]] = None


class HotelOrderDetailQueryResponse(CtripBaseModel):
    LstHtlSettlement: Optional[list[HotelAccountSettlementInfo]] = None
    Status: Optional[ResponseStatus] = None
    TotalRecord: Optional[int] = None
    TotalSize: Optional[int] = None


class TrainOrderDetailsQueryRequest(CtripBaseModel):
    Auth: Optional[Authentification] = None
    AccountId: Optional[str] = None
    DateFrom: Optional[str] = None
    DateTo: Optional[str] = None
    BatchNo: Optional[str] = None
    SettlementType: Optional[str] = None
    RecordId: Optional[str] = None
    OrderId: Optional[int] = None
    JourneyNoList: Optional[list[str]] = None
    IsCompensation: Optional[bool] = None
    PageIndex: Optional[int] = None
    PageSize: Optional[int] = None
    SubBatchNoList: Optional[list[str]] = None


class TrainStandardGeoEntity(CtripBaseModel):
    CountryId: Optional[int] = None
    CountryName: Optional[str] = None
    CountryEnName: Optional[str] = None
    ProvinceId: Optional[int] = None
    ProvinceName: Optional[str] = None
    ProvinceEnName: Optional[str] = None
    CityId: Optional[int] = None
    CityName: Optional[str] = None
    CityEnName: Optional[str] = None
    DistrictId: Optional[int] = None
    DistrictName: Optional[str] = None
    DistrictEnName: Optional[str] = None
    CountryCode: Optional[str] = None


class TrainStandardGeoInfo(CtripBaseModel):
    DepartureInfo: Optional[TrainStandardGeoEntity] = None
    ArrivalInfo: Optional[TrainStandardGeoEntity] = None


class TrainOrderSettlementDetail(CtripBaseModel):
    RecordID: Optional[str] = None
    OrderID: Optional[int] = None
    CorpId: Optional[str] = None
    AccountID: Optional[int | str] = None
    UID: Optional[str] = None
    DetailType: Optional[str] = None
    PassengerName: Optional[str] = None
    Price: Optional[Decimal] = None
    ServerFee: Optional[Decimal] = None
    CancelFee: Optional[Decimal] = None
    InsureFee: Optional[Decimal] = None
    PaperTicketFee: Optional[Decimal] = None
    DeliverFee: Optional[Decimal] = None
    ReBookingServiceFee: Optional[Decimal] = None
    RefundTicketServiceFee: Optional[Decimal] = None
    RealAmount: Optional[Decimal] = None
    BatchNo: Optional[str] = None
    SettlementType: Optional[str] = None
    Createtime: Optional[str] = None
    ChangeLasttime: Optional[str] = None
    OrderType: Optional[int] = None
    SubAccCheckBatchNo: Optional[str] = None
    TripID: Optional[int] = None
    SettlementCurrency: Optional[str] = None
    GrabServiceFee: Optional[Decimal] = None
    PostServiceFee: Optional[Decimal] = None
    RealAmountHasPost: Optional[Decimal] = None
    IsChecked: Optional[bool] = None
    SubDetailType: Optional[str] = None
    InvoiceIds: Optional[list[int]] = None
    BatchStartDate: Optional[str] = None
    BatchEndDate: Optional[str] = None
    AfterTakeTicketFee: Optional[Decimal] = None
    EstimatePrice: Optional[Decimal] = None
    EstimaAmount: Optional[Decimal] = None
    PurchaseFee: Optional[Decimal] = None
    PayMixFlag: Optional[bool] = None
    PersonalPayTicketFee: Optional[Decimal] = None
    PersonalPayServiceFee: Optional[Decimal] = None
    PersonalPayOtherFee: Optional[Decimal] = None
    TrainChangePrice: Optional[Decimal] = None
    TrainOtherFee: Optional[Decimal] = None
    DealTime: Optional[str] = None
    ProductType: Optional[str] = None
    DepartureCountry: Optional[str] = None
    ArrivalCountry: Optional[str] = None
    Sequence: Optional[int] = None
    LoanServiceFee: Optional[Decimal] = None
    IntlIssueTicketFee: Optional[Decimal] = None
    DeductibleTax: Optional[Decimal] = None
    NotIncludeTaxPrice: Optional[Decimal] = None
    OnsiteRefundFlag: Optional[bool] = None
    TicketPrice: Optional[Decimal] = None
    PersonalPayAmountSummary: Optional[Decimal] = None
    TotalAmount: Optional[Decimal] = None
    AccountPayAmount: Optional[Decimal] = None
    PersonalPayAmount: Optional[Decimal] = None
    OfflineRefundRebookFlag: Optional[bool] = None
    CardPayFee: Optional[Decimal] = None
    ElectronicTicketFlag: Optional[bool] = None
    ElectronicTicketAvailableFlag: Optional[bool] = None
    RealDeductibleTax: Optional[Decimal] = None
    RealNonDeductibleTax: Optional[Decimal] = None
    delayRescheduleFee: Optional[Decimal] = None
    refundRescheduleFee: Optional[Decimal] = None
    PaymentType: Optional[str] = None
    voucherMatchFlag: Optional[bool] = None
    BookingFee: Optional[Decimal] = None


class TrainOrderSettlementOrder(CtripBaseModel):
    OrderId: Optional[int] = None
    OrderStatus: Optional[str] = None
    ServerFrom: Optional[str] = None
    UserName: Optional[str] = None
    OrderType: Optional[str] = None
    PaymentType: Optional[str] = None
    TargetDate: Optional[str] = None
    RefundTicketStatus: Optional[str] = None
    CorpTravelEndorsementId: Optional[str] = None
    ChangeTicketStatus: Optional[str] = None
    ConfirmPerson: Optional[str] = None
    ConfirmPersonCC: Optional[str] = None
    DefineValue1: Optional[str] = None
    DefineValue2: Optional[str] = None
    JouneryID: Optional[str] = None
    RcCodeID: Optional[str] = None
    RcCodeName: Optional[str] = None
    ShipAddressDetail: Optional[str] = None
    ShipReceiverName: Optional[str] = None
    PreEmployeeID: Optional[str] = None
    CostCenter1: Optional[str] = None
    CostCenter2: Optional[str] = None
    CostCenter3: Optional[str] = None
    CostCenter4: Optional[str] = None
    CostCenter5: Optional[str] = None
    CostCenter6: Optional[str] = None
    JourneyReason: Optional[str] = None
    Project: Optional[str] = None
    NeedBigInvoice: Optional[bool] = None
    RankName: Optional[str] = None
    RankNameEn: Optional[str] = None
    ConfirmPersonName: Optional[str] = None
    ConfirmPersonEID: Optional[str] = None
    ConfirmPerson2: Optional[str] = None
    ConfirmPerson2Name: Optional[str] = None
    ConfirmPerson2EID: Optional[str] = None
    ProjectCode: Optional[str] = None
    WorkCity: Optional[str] = None
    TripType: Optional[str] = None
    RCCodeDescVV: Optional[str] = None
    NewOrderStatus: Optional[str] = None
    NewOrderStatusName: Optional[str] = None
    PayWay: Optional[str] = None
    TransProvincial: Optional[str] = None
    ReservationType: Optional[str] = None
    PreEmail: Optional[str] = None
    PrepareApprovalStatus: Optional[int] = None


class TrainOrderSettlementPassenger(CtripBaseModel):
    PassengerNo: Optional[int] = None
    PassengerID: Optional[int] = None
    PassengerName: Optional[str] = None
    CorpUserID: Optional[str] = None
    EmployeeID: Optional[str] = None
    TicketPassengerName: Optional[str] = None
    IdentityTypeName: Optional[str] = None
    IdentityNo: Optional[str] = None
    TicketTypeName: Optional[str] = None
    CostCenter1: Optional[str] = None
    CostCenter2: Optional[str] = None
    CostCenter3: Optional[str] = None
    CostCenter4: Optional[str] = None
    CostCenter5: Optional[str] = None
    CostCenter6: Optional[str] = None
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
    PassengerEmail: Optional[str] = None
    passengerNamePinYin: Optional[str] = None


class TrainSeatData(CtripBaseModel):
    Id: Optional[int] = None
    Name: Optional[str] = None
    Price: Optional[Decimal] = None
    isStandard: Optional[bool] = None


class TrainData(CtripBaseModel):
    SeatList: Optional[list[TrainSeatData]] = None
    UseTime: Optional[int] = None
    TrainName: Optional[str] = None


class TrainOrderSettlementTicket(CtripBaseModel):
    TicketInfoID: Optional[int] = None
    TrainName: Optional[str] = None
    FirstSeatTypeName: Optional[str] = None
    TrainType: Optional[str] = None
    DepartureCityName: Optional[str] = None
    DepartureDate: Optional[str] = None
    DepartureStationName: Optional[str] = None
    DepartureStationEn: Optional[str] = None
    ArrivalCityName: Optional[str] = None
    ArrivalDate: Optional[str] = None
    ArrivalStationName: Optional[str] = None
    ArrivalStationEn: Optional[str] = None
    ElectronicOrderNo: Optional[str] = None
    CustomType: Optional[int] = None
    CustomDetail: Optional[str] = None
    TrainTicketType: Optional[str] = None
    TrainSeatPriceData: Optional[list[TrainData]] = None
    ChangeStatus: Optional[str] = None
    DealTicketPrice: Optional[Decimal] = None
    RebRefEstimateAmount: Optional[Decimal] = None
    DepartureCityID: Optional[int] = None
    DepartureDistrictCode: Optional[str] = None
    ArrivalCityID: Optional[int] = None
    ArrivalDistrictCode: Optional[str] = None
    ChangeCode: Optional[str] = None
    DealSeatNo: Optional[str] = None
    DealSeatName: Optional[str] = None
    DepartureProvinceId: Optional[int] = None
    DepartureProvinceName: Optional[str] = None
    DepartureLocationId: Optional[int] = None
    DepartureLocationName: Optional[str] = None
    DepartureLocationCategoryId: Optional[int] = None
    ArrivalProvinceId: Optional[int] = None
    ArrivalProvinceName: Optional[str] = None
    ArrivalLocationId: Optional[int] = None
    ArrivalLocationName: Optional[str] = None
    ArrivalLocationCategoryId: Optional[int] = None
    Sequence: Optional[int] = None
    RefundreasonCode: Optional[str] = None
    RefundreasonCodeDesc: Optional[str] = None
    IssueTicketTime: Optional[str] = None
    RebookTicketSuccessTime: Optional[str] = None
    RefundTicketSuccessTime: Optional[str] = None
    ChangePreApprovalId: Optional[str] = None
    RefundApprovalId: Optional[str] = None
    standard_geo_info: Optional[TrainStandardGeoInfo] = Field(default=None, alias="StandardGeoInfo")
    ChangeDescription: Optional[str] = None
    TicketStatusCode: Optional[str] = None
    PreApprovalNo: Optional[str] = None
    SubPreApprovalNo: Optional[str] = None
    PreApprovalStatus: Optional[int] = None


class TrainOrderSettlementTicketRelation(CtripBaseModel):
    OrderId: Optional[int] = None
    PassengerNo: Optional[int] = None
    PassengerID: Optional[int] = None
    TicketInfoID: Optional[int] = None
    OrderTicketID: Optional[int] = None
    RefundTicketStatusDesc: Optional[str] = None
    RefundAmountStatus: Optional[str] = None
    ChangeStatus: Optional[str] = None
    TicketType: Optional[str] = None


class TrainSettlementInsuranceInfo(CtripBaseModel):
    OrderId: Optional[int] = None
    InsuranceNo: Optional[int] = None
    PassengerNo: Optional[int] = None
    OrderTicketNo: Optional[int] = None
    PolicyNo: Optional[str] = None
    PolicyStatus: Optional[str] = None
    ProductShortName: Optional[str] = None


class TrainSettlementTicketInfo(TrainOrderSettlementTicket):
    OrderTicketID: Optional[int] = None
    RefundTicketStatusDesc: Optional[str] = None
    RefundAmountStatus: Optional[str] = None
    TicketType: Optional[str] = None
    TakeTicketStatus: Optional[str] = None
    FailReason: Optional[str] = None
    OriginalDealSeatName: Optional[str] = None


class TrainSettlementFinalTripInfo(CtripBaseModel):
    PassengerName: Optional[str] = None
    EmployeeID: Optional[str] = None
    TicketStatus: Optional[str] = None
    TrainName: Optional[str] = None
    SeatNumber: Optional[str] = None
    DepartureDate: Optional[str] = None
    DepartureDateUTC: Optional[str] = None
    ArrivalDate: Optional[str] = None
    ArrivalDateUTC: Optional[str] = None
    DepartureStationCode: Optional[str] = None
    ArrivalStationCode: Optional[str] = None
    PayAmount: Optional[Decimal] = None
    TicketID: Optional[str] = None
    DepartureProvinceName: Optional[str] = None
    DepartureCityName: Optional[str] = None
    ArrivalProvinceName: Optional[str] = None
    ArrivalCityName: Optional[str] = None
    DepartureCityID: Optional[int] = None
    ArrivalCityID: Optional[int] = None
    seatType: Optional[str] = None
    TicketType: Optional[str] = None
    Birthday: Optional[str] = None


class TrainSettlementElectronicInvoiceVoucher(CtripBaseModel):
    InvoiceNo: Optional[str] = None
    ElectronicTicketNo: Optional[str] = None
    FeeType: Optional[str] = None


class TrainSettlementInfo(CtripBaseModel):
    TrainSettlementDetail: Optional[TrainOrderSettlementDetail] = None
    TrainSettlementOrder: Optional[TrainOrderSettlementOrder] = None
    TrainSettlementPassenger: Optional[TrainOrderSettlementPassenger] = None
    TrainSettlementTicket: Optional[TrainOrderSettlementTicket] = None
    TrainSettlementTicketRelation: Optional[TrainOrderSettlementTicketRelation] = None
    LstTrainSettlementInsuranceInfo: Optional[list[TrainSettlementInsuranceInfo]] = None
    TrainSettlementTicketInfoList: Optional[list[TrainSettlementTicketInfo]] = None
    TrainSettlementFinalTripInfoList: Optional[list[TrainSettlementFinalTripInfo]] = None
    TrainSettlementElectronicInvoiceVoucherList: Optional[list[TrainSettlementElectronicInvoiceVoucher]] = None
    approval_flow_info: Optional[ApprovalFlowInfo] = Field(default=None, alias="ApprovalFlowInfo")


class TrainAccountSettlement(CtripBaseModel):
    AccountId: Optional[str | int] = None
    LstTrainSettlementDetail: Optional[list[TrainSettlementInfo]] = None


class TrainOrderDetailsQueryResponse(CtripBaseModel):
    LstTrainSettlement: Optional[list[TrainAccountSettlement]] = None
    Status: Optional[ResponseStatus] = None
    TotalRecord: Optional[int] = None
    TotalSize: Optional[int] = None


class CarOrderDetailsQueryRequest(CtripBaseModel):
    Auth: Optional[Authentification] = None
    AccountId: Optional[str] = None
    DateFrom: Optional[str] = None
    DateTo: Optional[str] = None
    BatchNo: Optional[str] = None
    SelType: Optional[str] = None
    RecordId: Optional[str] = None
    OrderId: Optional[int] = None
    JourneyNoList: Optional[list[str]] = None
    IsCompensation: Optional[bool] = None
    PageIndex: Optional[int] = None
    PageSize: Optional[int] = None
    SubBatchNoList: Optional[list[str]] = None


class CarSettlementBaseInfo(CtripBaseModel):
    RecordId: Optional[int] = None
    BatchNo: Optional[str] = None
    CreateTime: Optional[str] = None
    DataChangeLastTime: Optional[str] = None
    ProductType: Optional[int] = None
    OrderID: Optional[int] = None
    SelType: Optional[str] = None
    DelType: Optional[str] = None
    CtripCardNo: Optional[str] = None
    UID: Optional[str] = None
    Amount: Optional[Decimal] = None
    CarAddTaxAmount: Optional[Decimal] = None
    CarBasicFeeDetail: Optional[str] = None
    CarValueAddFee: Optional[Decimal] = None
    CarValueAddFeeDetail: Optional[str] = None
    PenaltyFee: Optional[Decimal] = None
    RealAmount: Optional[Decimal] = None
    ServerFee: Optional[Decimal] = None
    ExpressFee: Optional[Decimal] = None
    OrderType: Optional[int] = None
    SubAccCheckBatchNo: Optional[str] = None
    TripID: Optional[int] = None
    SettlementCurrency: Optional[str] = None
    PostServiceFee: Optional[Decimal] = None
    RealAmountHasPost: Optional[Decimal] = None
    IsChecked: Optional[bool] = None
    InvoiceIds: Optional[list[int]] = None
    BatchNoStartDate: Optional[str] = None
    BatchNoEndDate: Optional[str] = None
    CorpID: Optional[str] = None
    AccountID: Optional[int | str] = None
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
    LoanServiceFee: Optional[Decimal] = None
    PayMixFlag: Optional[str] = None
    PersonAmount: Optional[Decimal] = None
    TotalAmount: Optional[Decimal] = None
    AccountPayAmount: Optional[Decimal] = None
    PersonalPayAmount: Optional[Decimal] = None
    CardPayFee: Optional[Decimal] = None
    PaymentType: Optional[str] = None


class CarOrderBaseInfo(CtripBaseModel):
    OrderID: Optional[int] = None
    AuthorizeStatus: Optional[str] = None
    CanCancelOrder: Optional[bool] = None
    CarControlItems: Optional[int] = None
    ChannelType: Optional[int] = None
    ContactEmail: Optional[str] = None
    ContactMobile: Optional[str] = None
    ContactName: Optional[str] = None
    CorpTravelEndorsementId: Optional[str] = None
    CtripCarBookFailCode: Optional[str | int] = None
    CtripCarBookFailReason: Optional[str] = None
    DealAmount: Optional[Decimal] = None
    FeeType: Optional[str] = None
    LanguageCode: Optional[str] = None
    NeedInvoice: Optional[bool] = None
    OrderAmount: Optional[Decimal] = None
    OrderDate: Optional[str] = None
    OrderStatus: Optional[str] = None
    OrderType: Optional[int] = None
    PaymentStatus: Optional[str] = None
    PaymentType: Optional[str] = None
    PolicyID: Optional[str] = None
    ReachCarControl: Optional[str] = None
    ReachTravel: Optional[str] = None
    ServerFrom: Optional[str] = None
    ServiceFee: Optional[Decimal] = None
    TripID: Optional[int] = None
    Uid: Optional[str] = None
    UserName: Optional[str] = None
    PreEmployeeID: Optional[str] = None
    EndChargeAmount: Optional[Decimal] = None
    RankName: Optional[str] = None
    RankNameEn: Optional[str] = None
    ConfirmPerson: Optional[str] = None
    ConfirmPersonEID: Optional[str] = None
    ConfirmPersonName: Optional[str] = None
    AccntAmount: Optional[Decimal] = None
    PersonAmount: Optional[Decimal] = None
    HasMixedPay: Optional[bool] = None
    ReservationType: Optional[str] = None
    PreEmail: Optional[str] = None
    Currency: Optional[str] = None
    OrderDateUTC: Optional[str] = None


class CarOrderCorpInfo(CtripBaseModel):
    CorpId: Optional[str | int] = None
    CorpName: Optional[str] = None
    AccountId: Optional[int | str] = None
    SubAccountId: Optional[int | str] = None
    BookType: Optional[str] = None
    CostCenter1: Optional[str] = None
    CostCenter2: Optional[str] = None
    CostCenter3: Optional[str] = None
    CostCenter4: Optional[str] = None
    CostCenter5: Optional[str] = None
    CostCenter6: Optional[str] = None
    JourneyReason: Optional[str] = None
    Project: Optional[str] = None
    DefineValue: Optional[str] = None
    DefineValue2: Optional[str] = None
    JouneryId: Optional[str] = None
    RcCodeId: Optional[str] = None
    RcCodeName: Optional[str] = None
    TripBookPolicy: Optional[str] = None
    TripPayPolicy: Optional[str] = None
    ProjectCode: Optional[str] = None
    SubPreApprovalNo: Optional[str] = None
    PreApprovalStatus: Optional[int] = None


class CarOrderPassengerInfo(CtripBaseModel):
    PassengerName: Optional[str] = None
    PassengerPhone: Optional[str] = None
    PassengerType: Optional[str] = None
    PassengerEmail: Optional[str] = None
    UserProperties: Optional[str] = None
    EmployeeID: Optional[str] = None
    CorpUserID: Optional[str] = None
    IdNumber: Optional[str] = None
    IdType: Optional[str] = None
    DistrictCode: Optional[str] = None
    CityId: Optional[int | str] = None
    CityName: Optional[str] = None
    CostCenter1: Optional[str] = None
    CostCenter2: Optional[str] = None
    CostCenter3: Optional[str] = None
    CostCenter4: Optional[str] = None
    CostCenter5: Optional[str] = None
    CostCenter6: Optional[str] = None
    CurrentStatus: Optional[int] = None
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
    PassengerNamePinYin: Optional[str] = None


class CarProductInfo(CtripBaseModel):
    ProductName: Optional[str] = None
    VendorName: Optional[str] = None
    UseTime: Optional[str] = None
    UserStartDate: Optional[str] = None
    UserEndDate: Optional[str] = None
    UseDate: Optional[str] = None
    DepartureCityId: Optional[int | str] = None
    DepartureDistrictCode: Optional[str] = None
    DepartureCityName: Optional[str] = None
    ArrivalCityId: Optional[int | str] = None
    ArrivalDistrictCode: Optional[str] = None
    ArrivalCityName: Optional[str] = None
    StartAddressName: Optional[str] = None
    StartAddressDetail: Optional[str] = None
    EndAddressName: Optional[str] = None
    EndAddressDetail: Optional[str] = None
    VehicleName: Optional[str] = None
    VehicleGroupId: Optional[int | str] = None
    VehicleGroupID: Optional[int | str] = None
    VehicleGroupName: Optional[str] = None
    VehicleGroupEnName: Optional[str] = None
    CarCapacity: Optional[int] = None
    CarDescription: Optional[str] = None
    FlightTrainNum: Optional[str] = None
    PatternType: Optional[int] = None
    ServiceBeginTime: Optional[str] = None
    ServiceEndTime: Optional[str] = None
    ActualDistance: Optional[Decimal] = None
    ActualTimeLength: Optional[Decimal] = None


class CarOrderDetailInfo(CtripBaseModel):
    OrderBaseInfo: Optional[CarOrderBaseInfo] = None
    CorpInfo: Optional[CarOrderCorpInfo] = None
    PassengerInfoList: Optional[list[CarOrderPassengerInfo]] = None
    SDProductInfo: Optional[CarProductInfo] = None
    ISProductInfo: Optional[CarProductInfo] = None
    CHProductInfo: Optional[CarProductInfo] = None
    OCHProductInfo: Optional[CarProductInfo] = None
    QuickProductInfo: Optional[CarProductInfo] = None
    CharterProductInfo: Optional[CarProductInfo] = None


class CarOrderSettlementInfo(CtripBaseModel):
    SettlementBaseInfo: Optional[CarSettlementBaseInfo] = None
    OrderDetail: Optional[CarOrderDetailInfo] = None
    approval_flow_info: Optional[ApprovalFlowInfo] = Field(default=None, alias="ApprovalFlowInfo")


class CarOrderAccountSettlement(CtripBaseModel):
    AccountId: Optional[int | str] = None
    CarSettlementDetailList: Optional[list[CarOrderSettlementInfo]] = None


class CarOrderDetailsQueryResponse(CtripBaseModel):
    CarOrderAccountSettlementList: Optional[list[CarOrderAccountSettlement]] = None
    Status: Optional[ResponseStatus] = None
    TotalRecord: Optional[int] = None
    TotalSize: Optional[int] = None
