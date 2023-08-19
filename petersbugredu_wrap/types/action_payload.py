class ActionPayload:
    def __init__(self, can_apply_for_distance: bool = True, can_print=None, can_add_homework: bool = True):
        """
        Class represents action payload API class
        :param can_apply_for_distance:
        :param can_print:
        """
        self.can_apply_for_distance = can_apply_for_distance
        self.can_print = can_print
        self.can_add_homework = can_add_homework
