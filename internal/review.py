class Review:
    def __init__(self, customer_id, message, star) -> None:
        self.__customer_id = customer_id
        self.__message = message
        self.__star = star
        
    @property
    def customer_id(self):
        return self.__customer_id
    @property
    def message(self):
        return self.__message
    @property
    def star(self):
        return self.__star
    
    def __str__(self):
        return {
            "customer_id" : self.__customer_id,
            "message" : self.__message,
            "star" : self.__star
        }