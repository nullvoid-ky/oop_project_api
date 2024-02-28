from uuid import uuid4, UUID

class Account:
    def __init__(self, username: str, password: str, pic_url: str = None, money: int = None) -> None:
        self.__id: UUID = uuid4()
        self.__username: str = username
        self.__password: str = password
        self.__pic_url: str = ""
        self.__money: int = 0
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
    def id(self) -> str:
        return str(self.__id)
    @property   
    def money(self) -> int:
        return self.__money
    def get_account_details(self) -> dict:
        return {
            "id": str(self.__id),
            "username": self.__username,
            "pic_url": self.__pic_url
        }
    
    def add_money(self, amount: int) -> int:
        self.__money += amount
        return self.__money
    
    def remove_money(self, amount: int) -> int:
        if self.__money - amount < 0:
            self.__money = 0
        else:
            self.__money -= amount
        return self.__money
    