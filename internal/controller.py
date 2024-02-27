from internal.account import Account

class Controller:
    def __init__(self) -> None:
        self.__account_list: list = []
        self.__booking_list: list = []

    def add_account(self, username: str, password: str) -> Account:
        account: Account = Account(username, password)
        self.__account_list.append(account)
        return account

    def get_account_by_username(self, username: str) -> Account | None:
        for account in self.__account_list:
            if account.username == username:
                return account
        return None