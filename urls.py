from typing import Mapping, Optional
from urllib.parse import urljoin


class RequestParams:
    def __init__(self, url: str, params: Optional[Mapping[str, str]] = None) -> None:
        self.url = url
        self.params = params


def token_url(baseUrl: str):
    # https://api.ocp.electrolux.one/one-account-authorization/api/v1/token
    return RequestParams(urljoin(baseUrl, "one-account-authorization/api/v1/token"))


def identity_providers_url(baseUrl: str, brand: str, username: str):
    # https://api.ocp.electrolux.one/one-account-user/api/v1/identity-providers?brand=electrolux&email={{username}}
    return RequestParams(
        urljoin(baseUrl, "one-account-user/api/v1/identity-providers"),
        {"brand": brand, "email": username},
    )
