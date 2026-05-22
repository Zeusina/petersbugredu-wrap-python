import dataclasses
import datetime
from typing import Any

from petersburgedu_wrap.types.action_payload import ActionPayload
from petersburgedu_wrap.types.estimate import Estimate
from petersburgedu_wrap.types.identity import Identity
from petersburgedu_wrap.types.task import Task


@dataclasses.dataclass
class LessonEntry:
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
    identity: Identity
    number: int
    datetime_from: datetime.datetime
    datetime_to: datetime.datetime
    subject_id: int
    subject_name: str
    content_name: str
    content_description: Any
    content_additional_material: Any
    tasks: list[Task]
    estimates: list[Estimate]
    action_payload: ActionPayload
