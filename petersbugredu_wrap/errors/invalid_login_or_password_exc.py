class InvalidLoginOrPasswordException(Exception):
    def __init__(self, *args):
        """
        Error raised when login or password are incorrect when user log in.
        :param args:
        """
        if args:
            self.message = args[0]
        else:
            self.message = None