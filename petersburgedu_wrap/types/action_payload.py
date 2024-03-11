import dataclasses


@dataclasses.dataclass
class ActionPayload:
    """
    Class represents action payload API entity
    :param can_apply_for_distance:
    :param can_print:
    :param can_add_homework:
    """
    can_apply_for_distance: bool = True
    can_print: bool = True
    can_add_homework: bool = True
