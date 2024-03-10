from uuid import uuid4, UUID
from datetime import datetime
from abc import ABC, abstractmethod

class AllAccount(ABC):
    def __init__(self, username, password) -> None:
        self._id: UUID = uuid4()
        self._display_name : str = username
        self._username: str = username
        self._password: str = password

    @abstractmethod
    def get_account_details(self) -> dict:
        pass


class Account(AllAccount):
    def __init__(self, username: str, password: str, gender: str, location: str, pic_url: str = "", amount: int = 0, age: int = 18) -> None:
        super().__init__(username, password)
        self._pic_url: str = pic_url
        self._amount: int = amount
        self._gender: str = gender
        self._location: str = location
        self._age: int = age
        self._transaction_list: list = []
        self._timestamp = datetime.now()

    @property
    def username(self) -> str:
        return self._username
    @property
    def gender(self) -> str:
        return self._gender
    @property
    def age(self) -> str:
        return self._age
    @property
    def pic_url(self) -> str:
        return self._pic_url
    @pic_url.setter
    def pic_url(self, url):
        self._pic_url = url
    @property
    def password(self) -> str:
        return self._password
    @property
    def display_name(self) -> str:
        return self._display_name
    @display_name.setter
    def display_name(self, name):
        self._display_name = name
    @property
    def id(self) -> UUID:
        return self._id
    @property
    def transaction_list(self) -> list:
        return self._transaction_list
    @property
    def amount(self) -> int:
        return self._amount
    @amount.setter
    def amount(self, amount):
        self._amount = amount
    @property
    def gender(self) -> str:
        return self._gender
    @property
    def location(self) -> str:
        return self._location
    @property
    def timestamp(self) -> datetime:
        return self._timestamp
    
    # MAKE TRANSACTION IMCOMPLETEE
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
    