class TryLoginBody:
    def __init__(self, username, password):
        self.username: str = username
        self.password: str = password

    def __eq__(self, other):
        if isinstance(other, TryLoginBody):
            return self.username == other.username and self.password == other.password
        return False

    def __hash__(self):
        return hash((self.username, self.password))
