from __future__ import annotations

import hashlib
from typing import Any

import httpx

from ..BaseClient import BaseClient
from ..sso.model import SSOLoginRequest, SSOTicketRequest, SSOTicketResponse


class SSOClient(BaseClient):
    API_BASE_URL = "https://ct.ctrip.com/corpservice"
    GET_TICKET_PATH = "/authorize/getticket"
    LOGIN_PATH = "/authorize/login"

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

    @staticmethod
    def _md5(value: str) -> str:
        return hashlib.md5(value.encode("utf-8")).hexdigest()

    @staticmethod
    def _stringify_form_value(value: Any) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    @staticmethod
    def _to_contract_field_name(name: str) -> str:
        if "_" not in name:
            return name
        return "".join(part[:1].upper() + part[1:] for part in name.split("_") if part)

    @staticmethod
    def login_url() -> str:
        return f"{SSOClient.API_BASE_URL}{SSOClient.LOGIN_PATH}"

    def build_ticket_request(
        self,
        *,
        app_key: str | None = None,
        app_security: str | None = None,
        token_type: str | None = None,
        group_id: int | None = None,
    ) -> SSOTicketRequest:
        return SSOTicketRequest(
            AppKey=app_key or self.XIECHEN_APP_KEY,
            AppSecurity=app_security or self.XIECHEN_APP_SECURITY,
            TokenType=token_type,
            GroupID=group_id,
        )

    def build_signature(
        self,
        *,
        uid: str = "",
        employee_id: str = "",
        email: str = "",
        ta: str = "",
        for_corp: int | str | None = 0,
        cost1: str = "",
        cost2: str = "",
        cost3: str = "",
        app_key: str | None = None,
        app_security: str | None = None,
    ) -> str:
        actual_app_key = app_key or self.XIECHEN_APP_KEY
        actual_app_security = app_security or self.XIECHEN_APP_SECURITY
        if not actual_app_key:
            raise ValueError("AppKey is required to build the SSO signature.")
        if not actual_app_security:
            raise ValueError("AppSecurity is required to build the SSO signature.")

        raw = "".join(
            [
                actual_app_key,
                uid,
                employee_id,
                email,
                ta,
                str(0 if for_corp is None else for_corp),
                cost1,
                cost2,
                cost3,
                self._md5(actual_app_security),
            ]
        )
        return self._md5(raw)

    def build_login_request(
        self,
        *,
        ticket: str,
        uid: str = "",
        employee_id: str = "",
        email: str = "",
        ta: str = "",
        for_corp: int = 0,
        cost1: str = "",
        cost2: str = "",
        cost3: str = "",
        app_key: str | None = None,
        app_security: str | None = None,
        **extra_fields: Any,
    ) -> SSOLoginRequest:
        if not ticket:
            raise ValueError("Ticket is required for SSO login.")
        if not any([uid, employee_id, email]):
            raise ValueError("UID, EmployeeID, and Email must provide at least one value.")

        actual_app_key = app_key or self.XIECHEN_APP_KEY
        if not actual_app_key:
            raise ValueError("AppKey is required for SSO login.")

        normalized_extra_fields = {
            self._to_contract_field_name(key): value
            for key, value in extra_fields.items()
        }

        signature = self.build_signature(
            uid=uid,
            employee_id=employee_id,
            email=email,
            ta=ta,
            for_corp=for_corp,
            cost1=cost1,
            cost2=cost2,
            cost3=cost3,
            app_key=actual_app_key,
            app_security=app_security,
        )

        return SSOLoginRequest(
            AppKey=actual_app_key,
            Ticket=ticket,
            UID=uid,
            EmployeeID=employee_id,
            Email=email,
            Signature=signature,
            TA=ta,
            ForCorp=for_corp,
            Cost1=cost1,
            Cost2=cost2,
            Cost3=cost3,
            **normalized_extra_fields,
        )

    def build_login_form_fields(
        self,
        *,
        ticket: str,
        uid: str = "",
        employee_id: str = "",
        email: str = "",
        ta: str = "",
        for_corp: int = 0,
        cost1: str = "",
        cost2: str = "",
        cost3: str = "",
        app_key: str | None = None,
        app_security: str | None = None,
        **extra_fields: Any,
    ) -> dict[str, str]:
        request = self.build_login_request(
            ticket=ticket,
            uid=uid,
            employee_id=employee_id,
            email=email,
            ta=ta,
            for_corp=for_corp,
            cost1=cost1,
            cost2=cost2,
            cost3=cost3,
            app_key=app_key,
            app_security=app_security,
            **extra_fields,
        )
        payload = request.model_dump(exclude_none=True)
        return {
            key: self._stringify_form_value(value)
            for key, value in payload.items()
        }

    async def request_ticket(
        self,
        *,
        app_key: str | None = None,
        app_security: str | None = None,
        token_type: str | None = None,
        group_id: int | None = None,
    ) -> SSOTicketResponse:
        payload = self.build_ticket_request(
            app_key=app_key,
            app_security=app_security,
            token_type=token_type,
            group_id=group_id,
        )
        async with httpx.AsyncClient(
            base_url=self.API_BASE_URL,
            limits=self.limits,
            timeout=self.timeout,
            transport=self.transport,
        ) as client:
            response = await client.post(
                self.GET_TICKET_PATH,
                json=payload.model_dump(exclude_none=True),
            )
            response.raise_for_status()
            return SSOTicketResponse.model_validate(response.json())

    async def get_ticket(
        self,
        *,
        app_key: str | None = None,
        app_security: str | None = None,
        token_type: str | None = None,
        group_id: int | None = None,
    ) -> str | None:
        response = await self.request_ticket(
            app_key=app_key,
            app_security=app_security,
            token_type=token_type,
            group_id=group_id,
        )
        return response.Token
