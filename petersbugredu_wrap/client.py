import json
import logging
import requests
from petersbugredu_wrap.utils import endpoints
from petersbugredu_wrap.errors.invalid_login_or_password_exc import InvalidLoginOrPasswordException


class Client:
    def __init__(self):
        self._token = None
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Client was created")

    def login(self, login: str, password: str):
        url = endpoints.LOGIN_URL
        self.logger.debug("Preparing payload & headers to login as %login%".replace("%login%", login))
        payload = (
            '{"type": "email", "login": "%login%", "activation_code": null, "password": "%password%", "_isEmpty": '
            'false}'.replace("%login%", login).replace("%password%", password))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/114.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        }
        self.logger.debug("Sending login request as %login%".replace("%login%", login))
        response = requests.request("POST", url, headers=headers, data=payload)
        self.logger.debug(
            "Request was successfully sent, status code: %code%".replace("%code%", str(response.status_code)))
        if response.status_code == 200:
            json_response: dict = json.loads(response.text)
            token = json_response.get("data", None).get("token", None)
            if token:
                self._token = token
            else:
                raise IndexError
        elif response.status_code == 400:
            raise InvalidLoginOrPasswordException
        else:
            raise ValueError
