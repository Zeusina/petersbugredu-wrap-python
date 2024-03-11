import dataclasses


@dataclasses.dataclass
class Subject: #TODO Add functional to class
    """
    Not implemented yet
    :param id:
    :param name:
    """
    id: int
    name: str

    def __post_init__(self):
        raise NotImplementedError
