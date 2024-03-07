import datetime

from internal.account import Account
from internal.availability import Availablility
from internal.review import Review

class Mate(Account):
    def __init__(self, username: str, password: str, amount: int=0):
        super().__init__(username, password)
        self.__availablility_list: list[Availablility] = []
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
    
    def add_availablility(self, date: datetime, detail: str) -> Availablility:
        availablility: Availablility = Availablility(date, detail)
        self.__availablility_list.append(availablility)
        return availablility
    
    def search_availablility(self, year: int, month: int, day: int) -> Availablility | None:
        for availablility in self.__availablility_list:
            if availablility.check_available(year, month, day):
                return availablility
        return None
    
    def book(self, customer: Account, year: int, month: int, day: int) -> Account | None:
        if isinstance(self.__booked_customer, type(None)):
            for availablility in self.__availablility_list:
                if availablility.check_available(year, month, day):
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
    
    
    def get_average_review_star(self):
        sum : float = 0
        for review in self.__review_list:
            sum += review.star
        if len(self.__review_list):
            return sum/len(self.__review_list)
        return None

    def get_review_amount(self):
        return len(self.__review_list)
    
    def get_account_created(self):
        return
        
    def search_review_by_id(self, review_id) -> Review | None:
        for review in self.__review_list:
            if review.validate_id(review_id):
                return review
        return None
    
    def add_review_mate(self, customer_id, message, star) -> Review | None:
        review = Review(customer_id, message, star)
        self.__review_list.append(review)
        return review
    
    def del_review_mate(self, review_id) -> Review | None:
        review = self.search_review_by_id(review_id)
        if review == None: 
            return None
        self.__review_list.remove(review)
        return review
    
    def get_review_mate(self) -> list:
        return self.review__review_list
    