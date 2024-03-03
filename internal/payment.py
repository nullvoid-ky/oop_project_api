from internal.customer import Customer
from internal.mate import Mate   

class Payment:
    def __init__(self, amount: int, is_mate_come: bool=None) -> None:
        self.__amount = amount
        self.__is_mate_come = is_mate_come

    def pay(self, customer: Customer, mate: Mate) -> None:
        customer - self.__amount
        mate + self.__amount
    @property
    def amount(self) -> int:
        return self.__amount