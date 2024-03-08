from internal.account import Account
from uuid import uuid4, UUID
from datetime import datetime

class Message:
    def __init__(self, sender: Account, text: str) -> None:
        self.__id: UUID = uuid4()
        self.__sender: Account = sender
        self.__text: str = text
        self.__timestamp: datetime = datetime.now()
        self.__is_edit: bool = False
    
    @property
    def id(self) -> UUID:
        return self.__id
    @property
    def is_edit(self) -> bool:
        return self.__is_edit
    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
    @property
    def text(self) -> str:
        return self.__text 
    @property
    def sender(self) -> Account:
        return self.__sender

    def set_text(self, text: str) -> None:
        self.__text = text
        self.__is_edit = True
    
    def get_message_details(self) -> dict:
        return {
            "id": str(self.__id),
            "sender": self.__sender.get_account_details(),
            "text": self.__text,
            "timestamp": self.__timestamp.strftime("%d/%m/%Y %H:%M")
        }

    # def get_sender_name(self) -> str:
    #     return self.__sender.username
    
    # def get_sender_account(self) -> Account:
    #     return self.__sender
    
    # def get_text(self) -> str:
    #     return self.__text
    
    # def get_timestamp(self) -> str:
    #     return self.__timestamp.strftime("%d/%m/%Y %H:%M:%S")
    