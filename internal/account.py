from uuid import uuid4, UUID

class Account:
    def __init__(self, username: str, password: str, gender: str, location: str, pic_url: str = None, money: int = 0) -> None:
        self.__id: UUID = uuid4()
        self.__display_name : str = username
        self.__username: str = username
        self.__password: str = password
        self.__pic_url: str = pic_url
        self.__money: int = money
        self.__gender: str = gender
        self.__location: str = location
        self.__transaction_list: list = []

    @property
    def username(self) -> str:
        return self.__username
    @property
    def pic_url(self) -> str:
        return self.__pic_url
    @property
    def password(self) -> str:
        return self.__password
    @property
    def display_name(self) -> str:
        return self.__display_name
    @property
    def id(self) -> UUID:
        return self.__id
    @property
    def transaction_list(self) -> list:
        return self.__transaction_list
    @property
    def money(self) -> int:
        return self.__money
    @property
    def gender(self) -> str:
        return self.__gender
    @property
    def location(self) -> str:
        return self.__location
    
    def get_account_details(self) -> dict:
        from internal.customer import Customer
        return {
            "id": str(self.__id),
            "username": self.__username,
            "pic_url": self.__pic_url,
            "role": "customer" if isinstance(self, Customer) else "mate", 
            "gender": self.__gender,
            "location": self.__location,
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
    