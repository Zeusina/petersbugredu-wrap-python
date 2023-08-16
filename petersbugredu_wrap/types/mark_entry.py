import datetime


class MarkEntry:
    def __init__(self, id: int, education_id: int, lesson_id: int, subject_id: int, subject_name: str, date: datetime.datetime,
                 estimate_value_code: str, estimate_value_name: str, estimate_type_code: str, estimate_type_name: str,
                 estimate_comment: str):
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
        self.estimate_type_name = estimate_type_name
        self.estimate_type_code = estimate_type_code
        self.estimate_comment = estimate_comment
        self.estimate_value_name = estimate_value_name
        self.estimate_value_code = estimate_value_code
        self.date = date
        self.subject_name = subject_name
        self.subject_id = subject_id
        self.lesson_id = lesson_id
        self.id = id
        self.education_id = education_id
