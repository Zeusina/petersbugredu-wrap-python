import dataclasses
from typing import Any


@dataclasses.dataclass
class Task:
    """
            Class represents task in API
            :param task_name:
            :param task_code:
            :param task_kind_code:
            :param task_kind_name:
            :param files:
    """
    task_name: str
    task_code: Any
    task_kind_code: str
    task_kind_name: str
    files: list
