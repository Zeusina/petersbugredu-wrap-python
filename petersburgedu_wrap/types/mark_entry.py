import dataclasses
import datetime


@dataclasses.dataclass
class MarkEntry:
    """
            Class represents mark entry in API
            :param id:
            :param education_id:
            :param lesson_id:
            :param subject_id:
            :param subject_name:
            :param date:
            :param estimate_value_code:
            :param estimate_value_name:
            :param estimate_type_code:
            :param estimate_type_name:
            :param estimate_comment:
    """
    id: int
    education_id: int
    lesson_id: int
    subject_id: int
    subject_name: str
    date: datetime.datetime
    estimate_value_code: str
    estimate_value_name: str
    estimate_type_code: str
    estimate_type_name: str
    estimate_comment: str
