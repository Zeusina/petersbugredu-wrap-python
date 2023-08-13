class ActionPayload:
    def __init__(self, can_apply_for_distance: bool, can_print=None):
        """
        Class represents action payload API class
        :param can_apply_for_distance:
        :param can_print:
        """
        self.can_apply_for_distance = can_apply_for_distance
        self.can_print = can_print
