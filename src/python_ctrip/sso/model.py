from __future__ import annotations

from typing import Optional

from ..ctrip_base_model import CtripBaseModel


class SSOTicketRequest(CtripBaseModel):
    AppKey: Optional[str] = None
    AppSecurity: Optional[str] = None
    TokenType: Optional[str] = None
    GroupID: Optional[int] = None


class SSOTicketResponse(CtripBaseModel):
    Token: Optional[str] = None
    Code: Optional[int] = None
    Message: Optional[str] = None
    Success: Optional[bool] = None


class SSOLoginRequest(CtripBaseModel):
    AppKey: Optional[str] = None
    Ticket: Optional[str] = None
    UID: str = ""
    EmployeeID: str = ""
    Email: str = ""
    Signature: Optional[str] = None
    TA: str = ""
    ForCorp: int = 0
    Cost1: str = ""
    Cost2: str = ""
    Cost3: str = ""
    Cost4: Optional[str] = None
    Cost5: Optional[str] = None
    Cost6: Optional[str] = None
    JourneyReason: Optional[str] = None
    Project: Optional[str] = None
    DefineFlag: Optional[str] = None
    DefineFlag2: Optional[str] = None
    SearchType: Optional[str] = None
    AuthorizerEmployeeID: Optional[str] = None
    Authorizer2EmployeeID: Optional[str] = None
    InitPage: Optional[str] = None
    CurrentLang: Optional[str] = None
    OrderId: Optional[str] = None
    OnlyInitPage: Optional[bool] = None
    AllowChangeApproval: Optional[str] = None
    ProductType: Optional[str] = None
    ProductId: Optional[str] = None
    OrderSuccessBackUrl: Optional[str] = None
    CustomAuthCallBackUrl: Optional[str] = None
    ErrorBackUrl: Optional[str] = None


__all__ = [
    "CtripBaseModel",
    "SSOLoginRequest",
    "SSOTicketRequest",
    "SSOTicketResponse",
]
