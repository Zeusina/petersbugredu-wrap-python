import datetime
import json
import logging

import requests

from petersbugredu_wrap.types.action_payload import ActionPayload
from petersbugredu_wrap.types.mark_entry import MarkEntry
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

    def get_mark_list_by_period(self, date_from: datetime.date, date_to: datetime.date, education_number: int = 0)\
            -> list[MarkEntry]:
        """
        Function for getting mark list from API
        :param date_from:
        :param date_to:
        :param education_number:
        :return:
        """
        url = ((endpoints.MARKS_BY_DATE_URL
                .replace("{{education_id}}", str(self.educations[education_number].education_id))
                .replace("{{date_from}}", date_from.strftime("%d.%m.%Y")))
               .replace("{{date_to}}", date_to.strftime("%d.%m.%Y")))
        cookie = {"X-JWT-Token": self._token}
        self.logger.debug("Data for get marks by period prepaired")
        pages = []
        with requests.session() as session:
            response = session.request("GET", url.replace("{{page}}", "0"), cookies=cookie)
            self.logger.debug("Made request 1st page of marks with status code %code%"
                              .replace("%code%", str(response.status_code)))
            pages.append(json.loads(response.text))
            total_pages: int = pages[0]["data"]["total_pages"]
            if total_pages > 1:
                for page_number in range(2, total_pages + 1):
                    response = session.request("GET", url.replace("{{page}}", str(page_number)), cookies=cookie)
                    pages.append(json.loads(response.text))
                    self.logger.debug("Made request %page% page of marks with status code %code%"
                                      .replace("%code%", str(response.status_code)).replace("%page%", str(page_number)))
        marks = []
        for page in pages:
            for entry in page["data"]["items"]:
                id = entry["id"]
                education_id = entry["education_id"]
                lesson_id = entry.get("lesson_id", 0)
                subject_id = entry["subject_id"]
                subject_name = entry["subject_name"]
                date = datetime.datetime.strptime(entry["date"], "%d.%m.%Y")
                estimate_value_code = entry.get("estimate_value_code", "")
                estimate_value_name = entry.get("estimate_value_name", "")
                estimate_type_code = entry.get("estimate_type_code", "")
                estimate_type_name = entry.get("estimate_type_name", "")
                estimate_comment = entry.get("estimate_comment", "")
                mark_entry = MarkEntry(
                    id=id,
                    education_id=education_id,
                    lesson_id=lesson_id,
                    subject_id=subject_id,
                    subject_name=subject_name,
                    date=date,
                    estimate_value_code=estimate_value_code,
                    estimate_value_name=estimate_value_name,
                    estimate_type_code=estimate_type_code,
                    estimate_type_name=estimate_type_name,
                    estimate_comment=estimate_comment)
                marks.append(mark_entry)
        return marks
