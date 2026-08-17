from __future__ import annotations

from collections.abc import Sequence

import httpx

from ..BaseClient import BaseClient
from ..details.model import (
    Authentification,
    CarOrderDetailsQueryRequest,
    CarOrderDetailsQueryResponse,
    TicketRequest,
    TicketResponse,
)


class CarOrderDetailsQuery(BaseClient):
    """Query car-service settlement details through Ctrip's settlement API."""

    API_BASE_URL = "https://ct.ctrip.com"
    TICKET_PATH = "/SwitchAPI/Order/Ticket"
    SETTLEMENT_PATH = "/switchapi/CarOrderSettlement/SearchSettlementCarOrderDetail"

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

    def build_ticket_request(self, app_key: str | None = None, app_security: str | None = None) -> TicketRequest:
        return TicketRequest(appKey=app_key or self.XIECHEN_APP_KEY, appSecurity=app_security or self.XIECHEN_APP_SECURITY)

    def build_auth(self, ticket: str, app_key: str | None = None) -> Authentification:
        return Authentification(AppKey=app_key or self.XIECHEN_APP_KEY, Ticket=ticket)

    def build_query_request(self, *, ticket: str | None = None, app_key: str | None = None, **kwargs) -> CarOrderDetailsQueryRequest:
        return CarOrderDetailsQueryRequest(Auth=self.build_auth(ticket, app_key) if ticket else None, **kwargs)

    async def get_ticket(self, app_key: str | None = None, app_security: str | None = None) -> str | None:
        payload = self.build_ticket_request(app_key, app_security)
        async with httpx.AsyncClient(base_url=self.API_BASE_URL, limits=self.limits, timeout=self.timeout, transport=self.transport) as client:
            response = await client.post(self.TICKET_PATH, json=payload.model_dump())
            response.raise_for_status()
            response_data = response.json()
            return TicketResponse.model_validate(response_data.get("TicketResult", response_data)).Ticket

    async def query(self, request: CarOrderDetailsQueryRequest) -> CarOrderDetailsQueryResponse:
        ticket = await self.get_ticket()
        request.Auth = self.build_auth(ticket or "")
        async with httpx.AsyncClient(base_url=self.API_BASE_URL, limits=self.limits, timeout=self.timeout, transport=self.transport) as client:
            response = await client.post(self.SETTLEMENT_PATH, params={"type": "json"}, json=request.model_dump())
            response.raise_for_status()
            return CarOrderDetailsQueryResponse.model_validate(response.json())

    async def query_by_date(
        self,
        date_from: str,
        date_to: str,
        *,
        account_id: str | int | None = None,
        settlement_type: str | None = None,
        **kwargs,
    ) -> CarOrderDetailsQueryResponse:
        return await self.query(
            self.build_query_request(
                DateFrom=date_from,
                DateTo=date_to,
                AccountId=str(account_id) if account_id is not None else None,
                SelType=settlement_type,
                **kwargs,
            )
        )

    async def query_by_batch_no(self, batch_no: str, *, settlement_type: str | None = None, **kwargs) -> CarOrderDetailsQueryResponse:
        return await self.query(self.build_query_request(BatchNo=batch_no, SelType=settlement_type, **kwargs))

    async def query_by_sub_batch_nos(self, sub_batch_nos: Sequence[str], **kwargs) -> CarOrderDetailsQueryResponse:
        return await self.query(self.build_query_request(SubBatchNoList=list(sub_batch_nos), **kwargs))

    async def query_by_record_ids(self, record_ids: Sequence[int | str] | int | str, **kwargs) -> CarOrderDetailsQueryResponse:
        ids = [record_ids] if isinstance(record_ids, (int, str)) else record_ids
        return await self.query(self.build_query_request(RecordId=",".join(str(record_id) for record_id in ids), **kwargs))

    async def query_by_order_id(self, order_id: int, **kwargs) -> CarOrderDetailsQueryResponse:
        return await self.query(self.build_query_request(OrderId=order_id, **kwargs))
