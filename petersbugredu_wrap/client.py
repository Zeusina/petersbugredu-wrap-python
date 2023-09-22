import json
import logging
import requests

from petersbugredu_wrap.types.education import Education
from petersbugredu_wrap.utils import endpoints, request_parameters
from petersbugredu_wrap.errors.invalid_login_or_password_exc import InvalidLoginOrPasswordException
from petersbugredu_wrap.types import Child, ActionPayload, Identity


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
        :rtype: list[Child]
        :return: list
        """
        url = endpoints.RELATED_CHILD_LIST_URL
        self.logger.info("Preparing data for getting child list")
        payload = {}
        headers = request_parameters.headers
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
            hash_uid = child.get("hash_uid", "")
            action_payload = ActionPayload(
                can_apply_for_distance=child["action_payload"].get("can_apply_for_distance", True),
                can_print=child["action_payload"].get("can_print", None))
            identity = Identity(id=child["identity"]["id"])
            educations: list[Education] = []
            for education in child["educations"]:
                push_subscribe = education.get("push_subscribe", "true")
                education_id = education["education_id"]
                group_id = education["group_id"]
                group_name = education.get("group_name", "")
                institution_id = education["institution_id"]
                institution_name = education.get("institution_name", "")
                is_active = education.get("is_active", None)
                distance_education = education.get("distance_education", False)
                distance_education_updated_at = education.get("distance_education_updated_at", "")
                parent_firstname = education.get("parent_firstname", "")
                parent_surname = education.get("parent_surname", "")
                parent_middlename = education.get("parent_middlename", "")
                parent_email = education.get("parent_email", "")
                jurisdiction_name = education.get("jurisdiction_name", "")
                jurisdiction_id = education["jurisdiction_id"]
                edu = Education(push_subscribe=push_subscribe,
                                education_id=education_id,
                                group_id=group_id,
                                group_name=group_name,
                                institution_id=institution_id,
                                institution_name=institution_name,
                                is_active=is_active,
                                distance_education=distance_education,
                                distance_education_updated_at=distance_education_updated_at,
                                parent_firstname=parent_firstname,
                                parent_surname=parent_surname,
                                parent_middlename=parent_middlename,
                                parent_email=parent_email,
                                jurisdiction_name=jurisdiction_name,
                                jurisdiction_id=jurisdiction_id)
                educations.append(edu)

            self.children.append(
                Child(
                    firstname=firstname,
                    surname=surname,
                    middlename=middlename,
                    educations=educations,
                    hash_uid=hash_uid,
                    action_payload=action_payload,
                    identity=identity,
                    token=self._token
                ))
        return self.children
