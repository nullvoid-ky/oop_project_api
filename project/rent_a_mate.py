from datetime import datetime

class Account:
    def __init__(self):
        self.chat_list = []
    
    def view_transaction(self):
        pass
    
    def set_name(self, name):
        self.name = name
    
    def set_picture(self, picture):
        self.picture = picture

class Customer(Account):
    def rent_mate(self):
        pass
    
    def cancel_mate(self):
        pass
    
    def pay(self):
        pass
    
    def review_mate(self):
        pass
    
    def add_money(self):
        pass

class Mate(Account):
    def __init__(self):
        super().__init__()
        self.__available_list = []
    
    def free_at(self, date):
        for available in self.__available_list:
            if available.date == date:
                return True
        return False

    def check_available(self):
        pass
    
    def confirm_booking(self):
        pass
    
    def update_available(self):
        pass
    
    def create_post(self):
        pass
    
    def withdraw(self):
        pass
    
    def set_available(self):
        pass

class Review:
    pass

class Payment:
    def create_transaction(self):
        pass
    
    def create_chat(self):
        pass

class Booking:
    def create_payment(self):
        pass

class Available:
    def __init__(self):
        self.location = ""
        self.time_start = ""
        self.time_end = ""
        self.date = ""
        self.is_rent = False
        self.is_available = False

class Transaction:
    def __init__(self):
        self.sender_account = None
        self.receiver_account = None
        self.amount = 0
        self.total = 0
        self.timestamp = datetime.now()

class Log:
    def __init__(self):
        self.message_type = ""
        self.message = ""
        self.timestamp = datetime.now()

class Leaderboard:
    def __init__(self):
        self.mate_list = []

class Post:
    def __init__(self):
        self.picture = ""
        self.description = ""
        self.timestamp = datetime.now()

class Message:
    def __init__(self):
        self.text = ""
        self.timestamp = datetime.now()

class Chat:
    def __init__(self):
        self.message_list = []
    
    def send_message(self):
        pass

class Server:

    def __init__(self) -> None:
        self.__people_list = []
        self.__mate_list = []

    def search_people_by_name(self, name : str):
        if not isinstance(name, str):
            return "Error"
        for people in self.__people_list:
            if people.check_name(name):
                return people
        return None
    
    def add_people(self, people):
        if not isinstance(people, People):
            print("-1")
        self.__people_list += [people]

    def sign_up_as_mate(self, people, username, password):
        if not isinstance(people, People):
            raise TypeError(f"Expected People, but got {type(people)} instead.")
        if not people.check_age_valid():
            raise ValueError("Age must be over 18.")
        
    
    def sign_up_as_customer(self, people, username, password):
        if not isinstance(people, People):
            raise TypeError(f"Expected People, but got {type(people)} instead.")
        if not people.check_age_valid():
            raise ValueError("Age must be over 18.")

    def login(self, username, password):
        pass 

    def create_mate_account(self):
        pass
    
    def create_customer_account(self):
        pass
    
    def view_mate_list(self):
        pass
    
    def view_post(self):
        pass
    
    def view_mate_info(self):
        pass
    
    def send_money(self):
        pass
    
    def create_transaction(self):
        pass
    
    def create_log(self):
        pass
    
    def search_mate_by_name(self):
        pass
    
    def search_mate_by_id(self):
        pass
    
    def search_mate_by_location(self):
        pass
    
    def search_mate_by_available(self):
        this_mate_list = []
        date = datetime.today()
        for mate in self.__mate_list:
            if mate.free_at(date):
                this_mate_list += [mate]
        print(this_mate_list)
                
    
    def search_mate_by_type(self):
        pass
    
    def get_leaderboard(self):
        pass


class People:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.gender = gender
    
    def check_name(self, name):
        return name == self.__name
    
    def check_age_valid(self):
        return self.__age >= 18
        

web = Server()
web.add_people( People("Tamtikorn", 19, 0))
web.add_people( People("Thanatchaya", 19, 1))
web.add_people( People("Nakul", 19, 0))
web.add_people( People("TajIsWomen", 19, 1))
web.add_people( People("NattapasIsWomen", 20, 1))

gan_people = web.search_people_by_name("Tamtikorn")
mook_people = web.search_people_by_name("Thanatchaya")
porche_people = web.search_people_by_name("Nakul")
taj_people = web.search_people_by_name("TajIsWomen")
nat_people = web.search_people_by_name("NattapasIsWomen")

web.sign_up_as_customer(gan_people, "ganxd123", "Ab12345.")
web.sign_up_as_customer(porche_people, "porchenarak", "Cd23456.")
web.sign_up_as_mate(mook_people, "mamoruuko","25032005")
web.sign_up_as_mate(taj_people, "tajnarak", "password")
web.sign_up_as_mate(nat_people, "transparent", "qwerty123")

gan_account = web.login("ganxd123", "Ab12345")
porche_account = web.login("porchenarak", "Cd23456")
mook_account = web.login("mamoruuko", "25032005")
taj_account = web.login("tajnarak", "password")
nat_account = web.login("transparent", "qwerty123")

account_list = web.search_mate_by_available()
# print(account_list)
gan_account.rent_mate(account_list[2])




