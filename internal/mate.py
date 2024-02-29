from internal.account import Account

class Mate(Account):
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)

    