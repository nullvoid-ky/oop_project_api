from fastapi import WebSocket  
from uuid import uuid4, UUID
from internal.message import Message

from internal.account import Account

class ChatRoomManeger:
    def __init__(self, account_1: Account, account_2: Account) -> None:
        self.__id: UUID = uuid4()
        self.__account_1: Account = account_1
        self.__account_2: Account = account_2
        self.__account_1_connection: WebSocket = None
        self.__account_2_connection: WebSocket = None
        self.__message_list: list[Message] = []

    @property
    def id(self) -> UUID:
        return self.__id
    @property
    def account_1(self) -> Account:
        return self.__account_1
    @property
    def account_2(self) -> Account:
        return self.__account_2
    @property
    def message_list(self) -> list:
        return self.__message_list
    
    async def connect(self, websocket: WebSocket, account: Account):
        connection: WebSocket = websocket
        await connection.accept()
        if self.__account_1 == account:
            self.__account_1_connection = connection
        elif self.__account_2 == account:
            self.__account_2_connection = connection
        print(f"User {account.get_account_details()} connected to chat room {self.__id}")

    def disconnect(self, websocket: WebSocket, account: Account):
        if self.__account_1 == account and self.__account_1_connection == websocket:
            self.__account_1_connection = None
        elif self.__account_2 == account and self.__account_2_connection == websocket:
            self.__account_2_connection = None

    async def add_message(self, message: str, account: Account):
        self.__message_list.append(Message(account, message))

    async def broadcast(self, message: str):
        if self.__account_1_connection:
            await self.__account_1_connection.send_text(message)
        if self.__account_2_connection:
            await self.__account_2_connection.send_text(message)

    def search_message_by_id(self, message_id: str) -> Message | None:
        for message in self.__message_list:
            if message.id == message_id:
                return message
        return None

    def get_chat_room_details(self) -> dict:
        return {
            "id": str(self.__id),
            "account_1": self.__account_1.get_account_details(),
            "account_2": self.__account_2.get_account_details()
        }