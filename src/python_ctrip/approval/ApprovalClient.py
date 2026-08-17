from __future__ import annotations

import logging

import httpx

from ..BaseClient import BaseClient
from ..approval.model import (
    Authentification,
    SaveApprovalRequest,
    SetApprovalResult,
    TicketRequest,
    TicketResponse,
)


class ApprovalClient(BaseClient):
    API_BASE_URL = "https://ct.ctrip.com"
    TICKET_PATH = "/SwitchAPI/Order/Ticket"
    SAVE_APPROVAL_PATH = "/switchapi/approval/save"

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
        self.logger = logging.getLogger("python.ctrip.ApprovalClient")

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

    def build_save_approval_request(
        self,
        approval_number: str,
        ctrip_card_no: str | None = None,
        employee_id: str | None = None,
        status: int = 1,
        ticket: str | None = None,
        app_key: str | None = None,
        **kwargs,
    ) -> SaveApprovalRequest:
        auth = None
        if ticket:
            auth = self.build_auth(ticket=ticket, app_key=app_key)

        return SaveApprovalRequest(
            ApprovalNumber=approval_number,
            Status=status,
            CtripCardNO=ctrip_card_no,
            EmployeeID=employee_id,
            Auth=auth,
            **kwargs,
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

    async def save_approval(
        self,
        request: SaveApprovalRequest,
    ) -> SetApprovalResult:
        actual_ticket = await self.get_ticket(app_key=self.XIECHEN_APP_KEY)
        request.Auth = self.build_auth(
            ticket=actual_ticket or "",
            app_key=self.XIECHEN_APP_KEY,
        )
        async with httpx.AsyncClient(
            base_url=self.API_BASE_URL,
            limits=self.limits,
            timeout=self.timeout,
            transport=self.transport,
        ) as client:
            payload = request.model_dump(exclude_none=True)
            self.logger.info("======save approval payload:======")
            self.logger.info(payload)
            self.logger.info("=================================")
            response = await client.post(
                self.SAVE_APPROVAL_PATH,
                json=payload,
            )
            response.raise_for_status()
            return SetApprovalResult.model_validate(response.json())
