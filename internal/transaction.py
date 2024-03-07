from datetime import datetime   
from internal.customer import Customer
from internal.mate import Mate

class Transaction:
    def __init__(self, sender: Customer, recipient: Mate, amount: int) -> None:
        self.__sender = sender
        self.__recipient = recipient
        self.__amount = amount
        self.__timestamp = datetime.now()

    @property
    def sender(self):
        return self.__sender
    @property
    def recipient(self):
        return self.__recipient
    @property
    def amount(self):
        return self.__amount
    @property
    def timestamp(self):
        return self.__timestamp

    def get_transaction_details(self) -> dict:
        return {
            "sender": str(self.sender.get_account_details()),
            "recipient": str(self.recipient.get_account_details()),
            "amount": self.amount,
            "timestamp": str(self.timestamp)
        }
