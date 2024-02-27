class Post:
    def __init__(self, description, picture, timestamp) :
        self.__description = description
        self.__picture = picture
        self.__timestamp = timestamp
        self.__post_list = []
        self.id 

    @property
    def description(self):
        return self.__description

    @property
    def picture(self):
        return self.__picture
    
    @property
    def timestamp(self):
        return self.__timestamp
        


