import uuid

class Account:
    def __init__(self, username: str, password: str) -> None:
        self.__id: uuid = uuid.uuid4()
        self.__display_name : str = username
        self.__username: str = username
        self.__password: str = password
        self.__pic_url: str = ""
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
    def id(self) -> uuid:
        return self.__id
    
    def get_account_details(self) -> dict:
        return {
            "id": self.__id,
            "username": self.__username,
            "pic_url": self.__pic_url
        }