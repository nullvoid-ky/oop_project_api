from internal.message import Message

class Chat:
    def __init__(self, owner1, owner2) -> None:
        """เก็บผู้ส่ง / รับ ใน msg
            เปลี่ยน sender, reciever เป็น acc ที่คู่กัน
        """
        self.__owner1 = owner1
        self.__owner2 = owner2
        self.__message_list = []
    
    def get_owner1(self):
        return self.__owner1

    def get_owner2(self):
        return self.__owner2
    
    def save_chat_log(self, message):
        if(isinstance(message, Message)):
            self.__message_list.append(message)
    
    def get_message_list(self):
        return self.__message_list
