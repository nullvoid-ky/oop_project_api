from uuid import uuid4, UUID
from datetime import datetime

class Account:
    def __init__(self, username: str, password: str, gender: str, location: str, pic_url: str = None, amount: int = 0, age: int = 18) -> None:
        self.__id: UUID = uuid4()
        self.__display_name : str = username
        self.__username: str = username
        self.__password: str = password
        self.__pic_url: str = pic_url
        self.__amount: int = amount
        self.__gender: str = gender
        self.__location: str = location
        self.__age: int = age
        self.__transaction_list: list = []
        self.__timestamp = datetime.now()
        
    @property
    def username(self) -> str:
        return self.__username
    @property
    def gender(self) -> str:
        return self.__gender
    @property
    def age(self) -> str:
        return self.__age
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
    def amount(self) -> int:
        return self.__amount
    @amount.setter
    def amount(self, amount):
        self.__amount = amount
    @property
    def gender(self) -> str:
        return self.__gender
    @property
    def location(self) -> str:
        return self.__location
    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
    
    def get_account_details(self) -> dict:
        from internal.customer import Customer
        return {
            "id": str(self.__id),
            "displayname": self.__display_name,
            "username": self.__username,
            "pic_url": self.__pic_url,
            "role": "customer" if isinstance(self, Customer) else "mate", 
            "gender": self.__gender,
            "location": self.__location,
            "timestamp": self.timestamp.strftime("%d/%m/%Y %H:%M:%S")
        }
    
    def add_transaction(self, transaction) -> None:
        from internal.transaction import Transaction
        if not isinstance(transaction, Transaction):
            raise TypeError(f"Expected transaction, but got {type(transaction)} instead.")
        self.__transaction_list.append(transaction)
    
    def __add__(self, amount: int) -> int:
        self.__amount += amount
        return self.__amount

    def __sub__(self, amount: int) -> int:
        if self.__amount - amount < 0:
            self.__amount = 0
        else:
            self.__amount -= amount
        return self.__amount
    