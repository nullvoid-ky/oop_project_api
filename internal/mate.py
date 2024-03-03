from internal.account import Account
from internal.availablility import Availablility
from internal.review import Review
# import datetime

class Mate(Account):
    def __init__(self, username: str, password: str, amount: int=0):
        super().__init__(username, password)
        self.__availablility_list = []
        self.__review_list = []
        self.__booked_customer = None
        self.__amount = amount
    @property
    def availablility_list(self) -> list[Availablility]:
        return self.__availablility_list
    @property
    def booked_customer(self) -> Account:
        return self.__booked_customer
    @property
    def amount(self) -> int:
        return self.__amount
    
    def add_availablility(self, availablility):
        if not isinstance(availablility, Availablility):
            raise TypeError(f"Expected availablility, but got {type(availablility)} instead.")
        self.__available_list += [availablility]
        return "Success"
    
    def book(self, customer: Account) -> Account | None:
        if isinstance(self.__booked_customer, type(None)):
            self.__booked_customer: Account = customer
            return self.__booked_customer
        return None

    def confirm_booking(self):
        pass
    
    def update_availablility(self):
        pass
    
    def add_post(self):
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