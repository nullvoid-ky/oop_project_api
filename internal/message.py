class Message:
    def __init__(self, sender, receiver, text, timestamp) -> None:
        self.__sender = sender
        self.__reciever = receiver
        self.__text = text
        self.__timestamp = timestamp
    
    def get_sender_name(self):
        return self.__sender.get_username()
    
    def get_text(self):
        return self.__text
    
    def get_timestamp(self):
        return self.__timestamp