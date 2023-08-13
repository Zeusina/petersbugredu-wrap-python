class Education:
    def __init__(self, push_subscribe: bool, education_id: int, group_id: int, group_name: str,
                 institution_id: int, institution_name: str, jurisdiction_id: int, jurisdiction_name: str, is_active,
                 distance_education: bool, distance_education_updated_at: str, parent_firstname: str,
                 parent_surname: str, parent_middlename: str, parent_email: str):
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
        self.parent_email = parent_email
        self.parent_middlename = parent_middlename
        self.parent_surname = parent_surname
        self.parent_firstname = parent_firstname
        self.distance_education_updated_at = distance_education_updated_at
        self.distance_education = distance_education
        self.is_active = is_active
        self.jurisdiction_name = jurisdiction_name
        self.jurisdiction_id = jurisdiction_id
        self.institution_name = institution_name
        self.institution_id = institution_id
        self.group_name = group_name
        self.group_id = group_id
        self.education_id = education_id
        self.push_subscribe = push_subscribe

