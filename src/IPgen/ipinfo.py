"""Create requests to http://ip-api.com/json/"""

import requests

from IPgen.util import is_ip_address


API_URL = "http://ip-api.com/json/"
HEADERS = {"Content-Type": "application/json"}


class APIRequest:
    """Class representation of an API request"""

    def __init__(self, api_url: str = None, headers: dict[str, str] = None):
        self._HEADERS = headers or {"Content-Type": "application/json"}
        self._API_URL = api_url or API_URL

    @property
    def HEADERS(self):
        return self._HEADERS

    @property
    def API_URL(self):
        return self._API_URL

    def send_API_request(self, IP: str) -> dict:
        if not is_ip_address(IP):
            raise Exception("Input is not a valid IP address")

        url = self.format_request(self.API_URL, IP)
        request = requests.get(url, headers=self.HEADERS)
        return self._get_result(request)

    def format_request(self, url: str, IP: str) -> str:
        return f"{url}{IP}"

    def _get_result(self, response: requests.Response) -> dict:
        if response.status_code == 200:
            return response.json()
        else:
            raise TimeoutError(f"ERROR: {response.status_code}")
