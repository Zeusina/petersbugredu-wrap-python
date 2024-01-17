import dataclasses
from typing import Any


@dataclasses.dataclass
class Estimate:
    """
            Class represents estimate API entity
            :param estimate_type_code:
            :param estimate_type_name:
            :param estimate_value_code:
            :param estimate_value_name:
            :param estimate_comment:
    """
    estimate_type_code: str
    estimate_type_name: str
    estimate_value_code: str
    estimate_value_name: str
    estimate_comment: Any
