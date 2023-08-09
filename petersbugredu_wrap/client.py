import json
import logging
import requests
from petersbugredu_wrap.utils import endpoints, request_parameters
from petersbugredu_wrap.errors.invalid_login_or_password_exc import InvalidLoginOrPasswordException
from petersbugredu_wrap.types import Child, Teacher


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
        headers = request_parameters.headers
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

    def get_child_list(self) -> list[Child]:
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

    def get_teacher_list(self, education_id: int) -> list[Teacher]:
        """
        Function to get list of teachers of concrete student
        :param education_id: Student education id
        :return: List of teachers
        """
        self.logger.debug("Started request to get teacher list")
        teacher_list = []
        url = endpoints.TEACHER_LIST_URL.replace("{{page}}", "1").replace("{{education_id}}", str(education_id))
        payload = {}
        headers = {}
        cookies = {
            "X-JWT-Token": self._token
        }

        response = requests.request("GET", url, headers=headers, data=payload, cookies=cookies)
        response_json = json.loads(response.text)
        self.logger.debug(
            "Get the response to get teacher list with %code% status code".replace("%code%", str(response.status_code)))
        if response.status_code != 200:
            return []
        for teacher in response_json["data"]["items"]:
            firstname = teacher.get("firstname", "")
            surname = teacher.get("surname", "")
            middlename = teacher.get("middlename", "")
            position_name = teacher.get("position_name", "")
            subjects = teacher.get("subjects", "")
            teacher_list.append(Teacher(
                firstname=firstname,
                surname=surname,
                middlename=middlename,
                position_name=position_name,
                subjects=subjects
            ))
        return teacher_list
