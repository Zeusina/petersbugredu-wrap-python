class Teacher:
    def __init__(self, firstname: str, surname: str, middlename: str, position_name: str, subjects: list[dict]):
        """
        Class Teacher represents school teachers
        :param firstname: Teacher firstname
        :param surname: Teacher surname
        :param middlename: Teacher middlename
        :param position_name: Name of position where teacher is
        :param subjects: List of teacher's subjects
        """
        self.firstname = firstname
        self.surname = surname
        self.middlename = middlename
        self.position_name = position_name
        self.subjects = subjects
        raise NotImplementedError
