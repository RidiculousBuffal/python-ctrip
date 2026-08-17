from __future__ import annotations

import httpx

from ..BaseClient import BaseClient
from ..people.model import (
    AuthenticationListRequest,
    AuthenticationResponseList,
    TicketRequest,
    TicketResponse, AuthenticationInfo,
)
import logging


class PeopleClient(BaseClient):
    TICKET_BASE_URL = "https://ct.ctrip.com"

    def __init__(
            self,
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
        self.logger = logging.getLogger("python.ctrip.PeopleClient")

    def build_ticket_request(
            self,
            app_key: str | None = None,
            app_security: str | None = None,
    ) -> TicketRequest:
        return TicketRequest(
            appKey=app_key or self.XIECHEN_APP_KEY,
            appSecurity=app_security or self.XIECHEN_APP_SECURITY,
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
                base_url=self.TICKET_BASE_URL,
                limits=self.limits,
                timeout=self.timeout,
        ) as client:
            response = await client.post(
                "/SwitchAPI/Order/Ticket",
                json=payload.model_dump(exclude_none=True),
            )
            response.raise_for_status()
            return TicketResponse.model_validate(response.json()).Ticket

    async def save_corp_cust_info_list(
            self,
            authInfo: list[AuthenticationInfo],
            corporateId: str = None
    ) -> AuthenticationResponseList:
        async with httpx.AsyncClient(
                base_url=self.BASE_URL,
                limits=self.limits,
                timeout=self.timeout,
        ) as client:
            ticket = await self.get_ticket()
            for a in authInfo:
                a.Authentication.SubAccountName = self.XIECHEN_SUB_ACCOUNT_NAME
            request = AuthenticationListRequest(Language='zh-CN', Appkey=self.XIECHEN_APP_KEY, Ticket=ticket,
                                                CorporationID=corporateId or self.XIECHEN_CORPORATE_ID,
                                                AuthenticationInfoList=authInfo)
            self.logger.info("======更新人事信息 payload:========")
            self.logger.info(request.model_dump(exclude_none=True))
            self.logger.info("=================================")
            response = await client.post(
                "/CorpCustService/SaveCorpCustInfoList",
                json=request.model_dump(exclude_none=True),
            )
            response.raise_for_status()
            return AuthenticationResponseList.model_validate(response.json())
