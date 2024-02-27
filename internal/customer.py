from internal.account import Account

class Customer(Account):
    def __init__(self, username: str, password: str) -> None:
        super().__init__(username, password)

    