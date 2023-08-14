import json
import logging

import requests

from petersbugredu_wrap.types.action_payload import ActionPayload
from petersbugredu_wrap.types.teacher import Teacher
from petersbugredu_wrap.types.identity import Identity
from petersbugredu_wrap.types.education import Education
from petersbugredu_wrap.utils import endpoints


class Child:
    def __init__(self, firstname: str, surname: str, middlename: str, educations: list[Education],
                 action_payload: ActionPayload, hash_uid: str, identity: Identity, token: str):
        """
        Class represents Children API entity
        :param firstname:
        :param surname:
        :param middlename:
        :param educations:
        :param action_payload:
        :param hash_uid:
        :param identity:
        :param token: JWT-Token for using methods
        """
        self.middlename = middlename
        self.firstname = firstname
        self.surname = surname
        self.educations = educations
        self.action_payload = action_payload
        self.hash_uid = hash_uid
        self.identity = identity
        self.logger = logging.getLogger("Child - %id%".replace("%id%", str(self.identity.id)))
        self._token = token
        self.logger.debug("Child successfully created")

    def get_teacher_list(self) -> list[Teacher]:
        """
        Function to get list of teachers of concrete student
        :return: List of teachers
        """
        education_id = self.educations[0].education_id
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
