import datetime

from petersbugredu_wrap.types import ActionPayload
from petersbugredu_wrap.types.estimate import Estimate
from petersbugredu_wrap.types.identity import Identity
from petersbugredu_wrap.types.task import Task


class LessonEntry:
    def __init__(self, identity: Identity, number: int, datetime_from: datetime.datetime,
                 datetime_to: datetime.datetime, subject_id: int,subject_name: str, content_name: str,
                 content_description, content_additional_material, tasks: list[Task], estimates: list[Estimate],
                 action_payload: ActionPayload):
        """
        Class represents lesson entry in API
        :param identity: 
        :param number: 
        :param datetime_from: 
        :param datetime_to: 
        :param subject_id: 
        :param subject_name: 
        :param content_name: 
        :param content_description: 
        :param content_additional_material: 
        :param tasks: 
        :param estimates: 
        :param action_payload: 
        """

        self.action_payload = action_payload
        self.estimates = estimates
        self.tasks = tasks
        self.content_additional_material = content_additional_material
        self.content_description = content_description
        self.content_name = content_name
        self.subject_name = subject_name
        self.subject_id = subject_id
        self.datetime_to = datetime_to
        self.datetime_from = datetime_from
        self.number = number
        self.identity = identity
