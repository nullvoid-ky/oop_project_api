import datetime
import uuid
from internal.mate import Mate
class Post:
    def __init__(self, writer, description: str, picture: str) :
        self.__writer: Mate = writer
        self.__description: str = description
        self.__picture: str = picture
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
            "account_detail": self.__writer.get_account_details(),
            "description": self.description,
            "picture": self.picture,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "id": str(self.id),
        }