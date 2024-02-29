from internal.account import Account
from internal.availablility import Availablility
from internal.review import Review
import datetime

class Mate(Account):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.__availablility_list = []
        self.__review_list = []    
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
    
    def add_review_mate(self, customer_id, message, star) -> Review | None:
        if not isinstance(customer_id , str):
            return None
        review = Review(customer_id, message, star)
        self.__review_list.append(review)
        return review