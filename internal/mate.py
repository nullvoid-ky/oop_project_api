from internal.account import Account
from internal.availablility import Availablility
import datetime

class Mate(Account):
    def __init__(self, user, username, password):
        super().__init__(user, username, password)
        self.__availablility_list = []
        self.post_list = []
    
    @property
    def availablility_list(self):
        return self.__availablility_list
    
    def add_availablility(self, availablility):
        if not isinstance(availablility, Availablility):
            raise TypeError(f"Expected availablility, but got {type(availablility)} instead.")
        self.__available_list += [availablility]
        return "Success"
    
    def confirm_booking(self):
        pass
    
    def update_availablility(self):
        pass
    
    def create_post(self):
        pass
    
    def withdraw(self):
        pass
    
    def set_availablility(self):
        pass
    
    # def create_post(self, title, pic):
    #     post = Post(title, pic)
        