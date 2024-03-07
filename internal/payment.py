from internal.account import Account

class Payment:
    def __init__(self, amount: int, is_mate_come: bool=None) -> None:
        self.__amount = amount
        self.__is_mate_come = is_mate_come

    def pay(self, sender: Account, receiver: Account) -> None:
        sender - self.__amount
        receiver + self.__amount
    @property
    def amount(self) -> int:
        return self.__amount