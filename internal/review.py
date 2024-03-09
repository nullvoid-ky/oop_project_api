from uuid import uuid4, UUID
from datetime import datetime
from internal.customer import Customer
class Review:
    def __init__(self, reviewer: Customer, message: str, star: int) -> None:
        self.__id : UUID = uuid4()
        self.__reviewer = reviewer
        self.__message : str = message
        self.__star : int = star 
        self.__timestamp = datetime.now()
        
    @property
    def id(self):
        return self.__id
    @property
    def reviewer(self):
        return self.__reviewer
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
            "timestamp" : str(self.__timestamp)
        }