from datetime import datetime

from uuid import uuid4, UUID
from internal.customer import Customer
from internal.mate import Mate
from internal.payment import Payment

class Booking:
    def __init__(self, customer: Customer, mate: Mate, payment: Payment = Payment(0, False)) -> None:
        self.__id = uuid4()
        self.__customer = customer
        self.__mate = mate
        self.__payment = payment
        self.__timestamp = datetime.now()
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
    
    def get_booking_detail(self) -> dict:
        return {
            "id": str(self.__id),
            "customer": self.__customer.get_account_details(),
            "mate": self.__mate.get_account_details(),
            "payment": self.__payment.amount,
            "timestamp": self.__timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }