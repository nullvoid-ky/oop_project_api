from uuid import uuid4, UUID
import datetime
class Review:
    def __init__(self, message, star) -> None:
        self.__id: UUID = uuid4()
        self.__message = message
        self.__star = star
        self.__timestamp = datetime.now()
        
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
    
    def get_review_details(self):
        return {
            "id" : str(self.__id),
            "message" : str(self.__message),
            "star" : str(self.__star),
            "timestamp" : str(self.__timestamp)
        }