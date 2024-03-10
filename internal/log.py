from datetime import datetime
class Log:
    def __init__(self, method, topic, description) -> None:
        self.__method : str = method # GET, POST, PUT, DELETE
        self.__topic :str = topic # Mate, Book. Error
        self.__description : str = description # Details text 
        self.__timestamp =  datetime.now()

        @property
        def method(self):
            return self.__method
        @property
        def topic(self):
            return self.__topic
        @property
        def description(self):
            return self.__description
        @property
        def timestamp(self):
            return self.__timestamp
        
        def get_log_details(self):
            return {
                "method" : self.__method,
                "topic" : self.__topic,
                "description" : self.__description,
                "timestamp" : self.__timestamp        
            }