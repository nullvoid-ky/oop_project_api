from internal.customer import Customer
from internal.mate import Mate   

class Payment:
    def __init__(self, amount):
        self.__amount = amount

    def pay(self, customer: Customer, mate: Mate) -> None:
        customer.remove_money(self.__amount)
        mate.add_money(self.__amount)
    @property
    def amount(self) -> int:
        return self.__amount
