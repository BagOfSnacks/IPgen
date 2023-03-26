"""Create requests to http://ip-api.com/json/"""

import requests

from IPgen.const import API_URL
from IPgen.util import is_ipv6_address, is_ipv4_address


class APIRequest:
    """Class representation of an API request"""

    def __init__(self):
        self.HEADERS = {'Content-Type': 'application/json'}

    def send_API_request(self, IP: str, URL: str = API_URL) -> dict:
        if not is_ipv4_address(IP) and not is_ipv6_address(IP):
            raise Exception('Input is not a valid IP address')

        url = self.format_request(URL, IP)
        request = requests.get(url, headers=self.HEADERS)
        return self._get_result(request)

    def format_request(self, url: str, IP: str) -> str:
        return f"{url}{IP}"

    def _get_result(self, response: requests.Response) -> dict:
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'ERROR: {response.status_code}')
