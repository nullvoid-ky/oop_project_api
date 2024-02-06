class Server:
    def __init__(self) -> None:
        self.__user_list = []
        self.__mate_list = []
        self.__amount = 0
        self.__lock = False
        self.__log_list = []

    @property
    def acc_list(self):
        return self.__user_list
    
    def show_mate_by_name(self, name):
        mate_list = []
        for mate in self.__mate_list:
            if mate.is_substr_by_name(name):
                mate_list += [name]
        return mate_list
    
    def _lock_server(self):
        self.__lock = True

    def _is_lock(self):
        return self.__lock
    
    def show_log_history(self):
        for log in self.__log_list:
            print(log)

    def say_log(self, type, message):
        pre_message = None
        error = True
        if type == -4:
            pass
        elif type == -3:
            pass
        elif type == -2:
            pre_message = "Duplicate Data"
        elif type == -1:
            pre_message = "Miss Match Instance"
            message = None
        elif type == 0:
            pass
        elif type == 1:
            pass
        elif type == 2:
            pass
        else:
            message = "Not Typed Error"
        if type > 0 and type <= 2:
            error = False
        log = Log(error,pre_message,message)
        self.__log_list.append(log)


    def create_user(self, user):
        if not isinstance(user, UserAccount):
            return self.say_log(-1, user)
        if user in self.__user_list:
            return self.say_log(-2, user)
        self.__user_list.append(user)
        return self.say_log(1, user)
        

    def create_mate(self, gender):
        pass    
        
class Platform():
    def __init__(self, server) -> None:
        self.__server = server
    
    def get_server(self):
        if self.__server._is_lock():
            return None
        self.__server._lock_server()
        return self.__server

    def search_mate_by_name(self, name):
        return self.__server.show_mate_by_name(name)
class Account:
    def __init__(self, display_name) -> None:
        self.__display_name = display_name
        self.__amount = 0

    def add_money(self, amount):
        pass
        
class UserAccount(Account):
    def __init__(self, gender, user_name, display_name, user_id) -> None:
        Account.__init__(self, display_name)
        self.__booking_list = []
        self.__user_name = user_name
        self.__gender = gender
        self.__user_id = user_id

    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def display_name(self):
        return self._Account__display_name
    
    def booking_mate_by_name(self, platform, mate_name, day, start, end):
        if not isinstance(mate_name, str):
            return -1
        mate = platform.search_mate_by_name(mate_name)
        Platform.say(mate)
        input()
        mate.is_avaiable(day, start, end)

class Mate(Account):
    def __init__(self, available, name) -> None:
        self.__available = False
        self.__name = name
        self.__time = None
        self.__cost = 0

    def set_cost(self, cost):
        pass
    
    def __set_available(self, logic):
        self.__available = logic

    def is_avaiable(self, day, start, end):
        if self.__available is False:
            return False
        if self.__time is None:
            return False
        day, start, end = self.__time.get_time()
        if start >= start and end <= end and day == day:
            self.__set_available(False)
            return True
        
    def is_substr_by_name(self, name):
        if name in self.__name:
            return True
        return False
        
    
class Girlfirend(Mate):
    gender = "F"
    def __init__(self) -> None:
        super().__init__()


class Boyfriend(Mate):
    gender = "M"
    def __init__(self) -> None:
        super().__init__()

class Booking:
    def __init__(self) -> None:
        self.__time

class Time:
    def __init__(self) -> None:
        self.__day
        self.__start
        self.__end

    def get_time(self):
        time_tuple = (self.__day, self.__start, self.__end)
        return time_tuple
    
class Log:
    def __init__(self, message_type, pre_message, message) -> None:
        if message_type:
            message_type = "Error"
        else:
            message_type = "Success"

        self.__message_type = message_type
        
        self.__pre_message = pre_message
        self.__message_id = message.user_id

        self.__message = message
        self.__message_display_name = self.__message.display_name
## TOdo Bug fix self.message
    def __str__(self) -> str:
        
        return f"{self.__message_type} {self.__pre_message} {self.__message.__class__.__name__}: {self.__message_display_name}#{self.__message_id}"
######################################################################################################
######################################################################################################
ce_rent_a_girlfriend = Platform(Server())
ce_rent_a_girlfriend_server = ce_rent_a_girlfriend.get_server()
ce_rent_a_girlfriend_server.create_user(UserAccount("M","Tamtikorn","GanThePro","10001"))
ce_rent_a_girlfriend_server.create_user(UserAccount("F","Narin","Alize","10002"))
ce_rent_a_girlfriend_server.create_user(UserAccount("F","Thanatchaya","mamoruko","10003"))
ce_rent_a_girlfriend_server.create_user(UserAccount("M","Nattanon","Nxck","10004"))
gan = ce_rent_a_girlfriend_server.acc_list[0]
alice = ce_rent_a_girlfriend_server.acc_list[1]
mook = ce_rent_a_girlfriend_server.acc_list[2]
nick = ce_rent_a_girlfriend_server.acc_list[3]
ce_rent_a_girlfriend_server.show_log_history()