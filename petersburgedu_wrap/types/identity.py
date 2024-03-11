import dataclasses


@dataclasses.dataclass
class Identity:
    """
            Class for implement identity parameter in API
            :param id: identity id
            :param uid: identity uid
    """
    id: int
    uid: str = None
