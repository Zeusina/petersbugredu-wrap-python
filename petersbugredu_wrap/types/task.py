class Task:
    def __init__(self, task_name: str, task_code, task_kind_code: str, task_kind_name: str, files: list):
        """
        Class represents task in API
        :param task_name: 
        :param task_code: 
        :param task_kind_code: 
        :param task_kind_name: 
        :param files: 
        """
        self.files = files
        self.task_kind_name = task_kind_name
        self.task_kind_code = task_kind_code
        self.task_code = task_code
        self.task_name = task_name
        raise NotImplementedError
    