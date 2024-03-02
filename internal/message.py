from uuid import uuid4, UUID

class Message:
    def __init__(self, sender, receiver, text, timestamp) -> None:
        self.__id: UUID = uuid4()
        self.__sender = sender
        self.__reciever = receiver
        self.__text = text
        self.__timestamp = timestamp
    
    @property
    def id(self) -> UUID:
        return self.__id
    
    def get_sender_name(self):
        return self.__sender.username
    
    def get_sender_account(self):
        return self.__sender
    
    def get_text(self):
        return self.__text
    
    def get_timestamp(self):
        return self.__timestamp