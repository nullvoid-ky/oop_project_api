from uuid import uuid4, UUID
from datetime import datetime

class Account:
    def __init__(self, username: str, password: str, pic_url: str = None, money: int = None, gender: str) -> None:
        self.__id: UUID = uuid4()
        self.__display_name : str = username
        self.__username: str = username
        self.__password: str = password
        self.__gender: str = gender
        self.__pic_url: str = ""
        self.__money: int = 0
        self.__transaction_list = []
        self.__timestamp = datetime.now()
        
    @property
    def username(self) -> str:
        return self.__username
    @property
    def gender(self) -> str:
        return self.__gender
    @property
    def pic_url(self) -> str:
        return self.__pic_url
    @pic_url.setter
    def pic_url(self, url):
        self.__pic_url = url
    @property
    def password(self) -> str:
        return self.__password
    @property
    def display_name(self) -> str:
        return self.__display_name
    @display_name.setter
    def display_name(self, name):
        self.__display_name = name
    @property
    def id(self) -> UUID:
        return self.__id
    @property
    def transaction_list(self) -> list:
        return self.__transaction_list
    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
    
    def get_account_details(self) -> dict:
        from internal.customer import Customer
        return {
            "id": str(self.__id),
            "username": self.username,
            "pic_url": self.pic_url,
            "role": "customer" if isinstance(self, Customer) else "mate",
            "timestamp": self.timestamp.strftime("%d/%m/%Y %H:%M:%S"),
            "display_name": self.display_name
        }
    
    def add_transaction(self, transaction) -> None:
        from internal.transaction import Transaction
        if not isinstance(transaction, Transaction):
            raise TypeError(f"Expected transaction, but got {type(transaction)} instead.")
        self.__transaction_list.append(transaction)
    
    def __add__(self, amount: int) -> int:
        self.__money += amount
        return self.__money

    def __sub__(self, amount: int) -> int:
        if self.__money - amount < 0:
            self.__money = 0
        else:
            self.__money -= amount
        return self.__money
    