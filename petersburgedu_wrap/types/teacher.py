import dataclasses


@dataclasses.dataclass
class Teacher:
    """
            Class Teacher represents school teachers returned by API
            :param firstname: Teacher firstname
            :param surname: Teacher surname
            :param middlename: Teacher middlename
            :param position_name: Name of position where teacher is
            :param subjects: List of teacher's subjects
    """
    firstname: str
    surname: str
    middlename: str
    position_name: str
    subjects: list[dict]
