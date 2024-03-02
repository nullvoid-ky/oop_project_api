from internal.message import Message
from uuid import uuid4, UUID

class Chat:
    def __init__(self, owner1, owner2) -> None:
        """เก็บผู้ส่ง / รับ ใน msg
            เปลี่ยน sender, reciever เป็น acc ที่คู่กัน
        """
        self.__id: UUID = uuid4()
        self.__owner1 = owner1
        self.__owner2 = owner2
        self.__message_list = []

    @property
    def id(self):
        return self.__id
    
    def get_owner1(self):
        return self.__owner1

    def get_owner2(self):
        return self.__owner2
    
    def save_chat_log(self, message):
        if(isinstance(message, Message)):
            self.__message_list.append(message)
            return message
        else:
            raise TypeError("Chat.save_chat_log() must receive message instance")
    
    def get_message_list(self):
        return self.__message_list
    
    def delete_message(self, message_id) -> list:
        self.__message_list = [message for message in self.__message_list if str(message.id) != message_id]
        return self.__message_list
    
    def edit_message(self, message_id, new_text) -> list:
        for message in self.__message_list:
            if str(message.id) == message_id:
                message.set_text(new_text)
                break
        return self.__message_list