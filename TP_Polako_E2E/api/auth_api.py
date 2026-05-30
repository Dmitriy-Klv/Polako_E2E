import os
from TP_Polako_E2E.api.base_api import BaseApi


class AuthApi(BaseApi):
    def login_and_save_token(self, email: str, password: str) -> str:
        response = self.session.post(
            f"{self.base_url}/api/auth/login",
            json={"email": email, "password": password},
        )
        response.raise_for_status()

        token = response.json().get("data", {}).get(
            "access_token"
        ) or response.json().get("access_token")

        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
            os.environ["AUTH_TOKEN"] = token

        return token