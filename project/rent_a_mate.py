import time

class Account:
    def __init__(self) -> None:
        self._user = None
        self._username = None
        self._password = None
        self._display_name = None
    
    @property
    def display_name(self):
        return self._display_name
    
    def add_display_name(self, nickname):
        self._display_name = nickname

    def validate_login(self, username, password):
        return (username == self._username and password == self._password)
    
    def view_transaction(self):
        pass
    
    def set_name(self, name):
        self.name = name
    
    def set_picture(self, picture):
        self.picture = picture

class Customer(Account):
    
    def __init__(self, user, username, password):
        super().__init__()
        self._user = user
        self._username = username
        self._password = password


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
    def __init__(self, user, username, password):
        super().__init__()
        self.__available_list = []
        self._user = user
        self._username = username
        self._password = password
    
    @property
    def available_list(self):
        return self.__available_list
    
    def is_available_from_date(self, date):
        for available in self.__available_list:
            if available.date == date:
                return True
        return False
    
    def add_available(self, available):
        if not isinstance(available, Available):
            raise TypeError(f"Expected available, but got {type(available)} instead.")
        self.__available_list += [available]
        return "Success"
    
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
    def __init__(self, loaction, time_start, time_end, date):
        self.location = loaction
        self.time_start = time_start
        self.time_end = time_end
        self.date = date
        self.is_rent = False
        
    def check_date(self, date):
        month = {
            "Jan" : 31,
            "Feb" : 60,
            "Mar" : 91,
            "Apr" : 121
        }
        self_days = month[self.date.split()[1]] + int(self.date.split()[0])
        check_days = month[date.split()[1]] + int(date.split()[0])
        # print(self_days)
        # print(check_days)

        return check_days <= self_days
        # print(self.date.split())
        # print(date.split())


class Transaction:
    def __init__(self):
        self.sender_account = None
        self.receiver_account = None
        self.amount = 0
        self.total = 0
        # self.timestamp = datetime.now()

class Log:
    def __init__(self):
        self.message_type = ""
        self.message = ""
        # self.timestamp = datetime.now()

class Leaderboard:
    def __init__(self):
        self.mate_list = []

class Post:
    def __init__(self):
        self.picture = ""
        self.description = ""
        # self.timestamp = datetime.now()

class Message:
    def __init__(self):
        self.text = ""
        # self.timestamp = datetime.now()

class Chat:
    def __init__(self):
        self.message_list = []
    
    def send_message(self):
        pass

class Controller:

    def __init__(self) -> None:
        self.__user_list = []
        self.__mate_list = []
        self.__chat_list = []

    @property
    def mate_list(self):
        return self.__mate_list
    
    @staticmethod
    def change_name_to_json(lst):
        name_dict = {}
        i = 1
        for item in lst:
            name_dict[i] = {"name" : item[0].display_name, "date" : item[1].date }
            i+=1
        return name_dict


    def print_accounts(self):
        for user in self.__user_list:
            print(user.account)
    def search_user_by_name(self, name : str):
        if not isinstance(name, str):
            return "Error"
        for user in self.__user_list:
            if user.check_name(name):
                return user
        return None
    
    def add_user(self, user):
        if not isinstance(user, User):
            print("-1")
        self.__user_list += [user]

    def sign_up_as_mate(self, user, username, password):
        if not isinstance(user, User):
            raise TypeError(f"Expected user, but got {type(user)} instead.")
        if not user.check_age_valid():
            raise ValueError("Age must be over 18.")
        account = Mate(user, username, password)
        user.add_account(account)
        self.__mate_list += [account]
        
    
    def sign_up_as_customer(self, user, username, password):
        if not isinstance(user, User):
            raise TypeError(f"Expected user, but got {type(user)} instead.")
        if not user.check_age_valid():
            raise ValueError("Age must be over 18.")
        user.add_account(Customer(user, username, password))

    def login(self, username, password):
        for user in self.__user_list:
            if user.account.validate_login(username, password):
                return user.account
        return None
    
    @staticmethod
    def is_substr(s1, s2):
        if s1 == None:
            return True
        if s2 == None:
            return False
        
        M = len(s1)
        N = len(s2)

        s1 = s1.lower()
        s2 = s2.lower()

        # A loop to slide pat[] one by one
        for i in range(N - M + 1):
    
            # For current index i,
            # check for pattern match
            for j in range(M):
                if (s2[i + j] != s1[j]):
                    break
    
            if j + 1 == M:
                return True
    
        return False
    
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
    
    def search_mate_by_name(self, name):
        new_list = []
        for mate in self.__mate_list:
            if Controller.is_substr(name, mate.display_name):
                    for available in mate.available_list: 
                        if available.check_date(get_date()):
                            new_list.append([mate,available])
        return new_list
    
    def search_mate_by_id(self):
        pass
    
    def search_mate_by_location(self):
        pass
    
    # def search_mate_by_available(self):
    #     this_mate_list = []
    #     date = time.today()
    #     for mate in self.__mate_list:
    #         if mate.free_at(date):
    #             this_mate_list += [mate]
    #     print(this_mate_list)
                
    
    def search_mate_by_type(self):
        pass
    
    def get_leaderboard(self):
        pass


class User:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.gender = gender
        self.__account = None

    @property
    def account(self):
        return self.__account

    def add_account(self, account):
        if not isinstance(account, Account):
            raise TypeError(f"Expected account, but got {type(account)} instead.")
        self.__account = account
        # print(type(account))

    def check_name(self, name):
        return name == self.__name
    
    def check_age_valid(self):
        return self.__age >= 18
        
def get_date():
    month = time.ctime().split()[1]
    days = time.ctime().split()[2]
    year = time.ctime().split()[-1]
    date = f"{days} {month} {year}"
    return date

def get_time():
    hr  = time.ctime().split()[3].split(":")[0]
    min = time.ctime().split()[3].split(":")[1]
    return f"{hr}:{min}"


