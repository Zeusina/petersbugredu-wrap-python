import json
import logging
import requests
from petersbugredu_wrap.utils import endpoints
from petersbugredu_wrap.errors.invalid_login_or_password_exc import InvalidLoginOrPasswordException
from petersbugredu_wrap.types.child import Child


class Client:
    def __init__(self) -> None:
        """
        Init function for Client class.
        Used for set parameters in Client class.
        :return:
        """
        self._token = None
        self.children: list[Child] = []
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Client was created")

    def login(self, login: str, password: str) -> None:
        """
        Function to log in petersburg educational portal with email and password.
        This function will get JWT token and store it as Client class parameter.
        :param login:
        :param password:
        :return:
        """
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
        
    def login_by_token(self, token: str) -> None:
        """
        This function will store JWT token as Client class parameter
        USE IF YOU HAVE JWT TOKEN
        :rtype: object
        :param token: 
        :return: 
        """
        self.logger.debug("Registered by token")
        self._token = token

    def get_child_list(self) -> list:
        """
        This function will get child list from petersburg educational portal, store it as class parameter and return
        it as list.
        :return: list
        """
        url = endpoints.RELATED_CHILD_LIST_URL
        self.logger.info("Preparing data for getting child list")
        payload = {}
        headers = {}
        cookies = {
            "X-JWT-Token": self._token
        }
        self.logger.debug("Sending request to API to get child list")
        response = requests.request("GET", url, headers=headers, data=payload, cookies=cookies)
        self.logger.debug(
            "Response with child list return %code% - status code".replace("%code%", str(response.status_code)))
        if response.status_code != 200:
            return []
        response_json: dict = json.loads(response.text)
        for child in response_json["data"]["items"]:
            firstname = child.get("firstname", "")
            surname = child.get("surname", "")
            middlename = child.get("middlename", "")
            educations = child["educations"]
            education_id = child["educations"][0]["education_id"]

            self.children.append(
                Child(
                    name=firstname,
                    surname=surname,
                    middlename=middlename,
                    educations=educations,
                    education_id=education_id
                ))
            return self.children
