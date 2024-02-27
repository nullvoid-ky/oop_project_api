from internal.account import Account
from internal.mate import Mate
from internal.customer import Customer

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
    
    def get_account_by_name(self, name: str) -> Account | None:
        for account in self.__account_list:
            if name in account.name:
                return account
        return None

    def get_mates(self) -> Account | None:
        mate_list = []
        for account in self.__account_list:
            if isinstance(account, Mate):
                mate_list.append(account)
        return None

    def get_customers(self) -> Account | None:
        customer_list = []
        for account in self.__account_list:
            if isinstance(account, Customer):
                customer_list.append(account)
        return None