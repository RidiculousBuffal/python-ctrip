import os

import httpx


class BaseClient:
    BASE_URL = "https://ct.ctrip.com/corpservice"
    limits = httpx.Limits(max_connections=1000, max_keepalive_connections=200)
    timeout = httpx.Timeout(None, connect=40.0)  # 设置时间限制

    def __init__(
        self,
        *,
        corporate_id: str | None = None,
        app_key: str | None = None,
        app_security: str | None = None,
        sub_account_name: str | None = None,
    ):
        self.XIECHEN_CORPORATE_ID = corporate_id or os.getenv("XIECHEN_CORPORATE_ID")
        self.XIECHEN_APP_KEY = app_key or os.getenv("XIECHEN_APP_KEY")
        self.XIECHEN_APP_SECURITY = app_security or os.getenv("XIECHEN_APP_SECURITY")
        self.XIECHEN_SUB_ACCOUNT_NAME = sub_account_name or os.getenv("XIECHEN_SUB_ACCOUNT_NAME")

    def build_ticket_model(self):
        return {
            "AppKey": self.XIECHEN_APP_KEY,
            "AppSecurity": self.XIECHEN_APP_SECURITY,
        }


    async def get_ticket(self):
        async with httpx.AsyncClient(base_url=self.BASE_URL,limits=self.limits,timeout=self.timeout) as client:
            response = await client.post('/authorize/getticket',json=self.build_ticket_model())
            res =  response.json()
            return res.get("Token",'')
