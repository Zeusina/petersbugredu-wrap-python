class Estimate:
    def __init__(self, estimate_type_code: str, estimate_type_name: str,
                 estimate_value_code: str, estimate_value_name: str, estimate_comment):
        """
        Class represents estimate API entity
        :param estimate_type_code:
        :param estimate_type_name:
        :param estimate_value_code:
        :param estimate_value_name:
        :param estimate_comment:
        """
        self.estimate_type_code = estimate_type_code
        self.estimate_type_name = estimate_type_name
        self.estimate_value_code = estimate_value_code
        self.estimate_value_name = estimate_value_name
        self.estimate_comment = estimate_comment
