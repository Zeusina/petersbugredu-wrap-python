class Child:
    def __init__(self, name: str, surname: str, middlename: str, education_id: int, educations: list):
        """
        This class will store information about child as class parameters/
        :param name:
        :param surname:
        :param middlename:
        :param education_id:
        :param educations:
        """
        self.middlename = middlename
        self.name = name
        self.surname = surname
        self.education_id = education_id
        self.educations = educations
