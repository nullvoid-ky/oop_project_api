from datetime import datetime   
from internal.customer import Customer
from internal.mate import Mate

class Transaction:
    def __init__(self, sender: Customer, recipient: Mate, amount: int) -> None:
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.now()

    def get_transaction_details(self) -> dict:
        return {
            "sender": str(self.sender.id),
            "recipient": str(self.recipient.id),
            "amount": self.amount,
            "timestamp": str(self.timestamp)
        }
