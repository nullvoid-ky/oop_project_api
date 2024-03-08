import datetime
import uuid

class Post:
    def __init__(self, description, picture) :
        self.__description = description
        self.__picture = picture
        self.__timestamp = datetime.datetime.now()
        self.__id = uuid.uuid4()

    @property
    def description(self):
        return self.__description
    @property
    def picture(self):
        return self.__picture
    @property
    def timestamp(self):
        return self.__timestamp
    @property
    def id(self):
        return self.__id
        
    def get_post_details(self) -> dict:
        return {
            "description": self.__description,
            "picture": self.__picture,
            "timestamp": self.__timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "id": str(self.__id),
        }