from uuid import uuid4, UUID
from internal.customer import Customer
import datetime

class Review:
    def __init__(self, message: str, star: int, customer:Customer) -> None:
        self.__id : UUID = uuid4()
        self.__message : str = message
        self.__star : int = star 
        self.__timestamp = datetime.datetime.now()
        self.__user = customer
        
    @property
    def id(self):
        return self.__id
    @property
    def message(self):
        return self.__message
    @property
    def star(self):
        return self.__star
    @property
    def timestamp(self):
        return self.__timestamp
    
    def get_review_details(self) -> dict:
        return {
            "id" : str(self.__id),
            "message" : str(self.__message),
            "star" : str(self.__star),
            "timestamp" : str(self.__timestamp),
            "user" : self.__user.get_account_details()
        }