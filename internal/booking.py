from uuid import uuid4, UUID
from internal.customer import Customer
from internal.mate import Mate
from internal.payment import Payment

class Booking:
    def __init__(self, customer: Customer, mate: Mate, payment: Payment = Payment(0)) -> None:
        self.__id = uuid4() 
        self.__customer = customer
        self.__mate = mate
        self.__payment = payment
    @property
    def customer(self) -> Customer:
        return self.__customer
    @property
    def id(self) -> UUID:
        return self.__id
    @property
    def mate(self) -> Mate:
        return self.__mate
    @property
    def payment(self) -> Payment:
        return self.__payment