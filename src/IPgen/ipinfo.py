"""Create requests to http://ip-api.com/json/"""

import requests


class APIRequest:
    """Class representation of an API request"""

    def __init__(self):
        self.API_URL = "http://ip-api.com/json/"
        self.HEADERS = {'Content-Type': 'application/json'}
        self.json_response = ...
        self.response_code: int = ...

    def send_API_request(self, IP: str) -> dict:
        url = self.format_request(self.API_URL, IP)
        request = requests.get(url, headers=self.HEADERS)
        return self._get_result(request)

    def format_request(self, url: str, IP: str) -> str:
        return f"{url}{IP}"

    def _get_result(self, response: requests.Response) -> dict:
        if response.status_code == 200:
            self.response_code = response.status_code
            self.json_response = response.json()
            return response.json()
        else:
            self.response_code = response.status_code
            self.json_response = None
            raise Exception(f'ERROR: {response.status_code}')
