import dataclasses
from typing import Any


@dataclasses.dataclass
class Education:
    """
           Class represent API education class
           :param push_subscribe:
           :param education_id:
           :param group_id:
           :param group_name:
           :param institution_id:
           :param institution_name:
           :param jurisdiction_id:
           :param jurisdiction_name:
           :param is_active:
           :param distance_education:
           :param distance_education_updated_at:
           :param parent_firstname:
           :param parent_surname:
           :param parent_middlename:
           :param parent_email:
           """
    push_subscribe: bool
    education_id: int
    group_id: int
    group_name: str
    institution_id: int
    institution_name: str
    jurisdiction_id: int
    jurisdiction_name: str
    is_active: Any
    distance_education: bool
    distance_education_updated_at: str
    parent_firstname: str
    parent_surname: str
    parent_middlename: str
    parent_email: str
