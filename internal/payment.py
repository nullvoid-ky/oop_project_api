from internal.customer import Customer
from internal.mate import Mate   

class Payment:
    def __init__(self, amount: int, is_mate_come: bool):
        self.__amount = amount
        self.__is_mate_come = False

    def pay(self, customer: Customer, mate: Mate) -> None:
        customer.remove_money(self.__amount)
        mate.add_money(self.__amount)
        # add_chat
    @property
    def amount(self) -> int:
        return self.__amount