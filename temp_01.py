class Server:
    def __init__(self) -> None:
        self.__user_list = []
        self.__mate_list = []
        self.__amount = 0

    def show_mate_by_name(self, name):
        mate_list = []
        for mate in self.__mate_list:
            if mate.is_substr_by_name(name):
                mate_list += [name]
        return mate_list
    
    def create_user(self, gender):
        pass    
    def create_mate(self, gender):
        pass    
        
class Platform:
    def __init__(self, server) -> None:
        self.__server = server
    
    def search_mate_by_name(self, name):
        return self.__server.show_mate_by_name(name)

class Account:
    def __init__(self, gender, user_name, display_name) -> None:
        self.__booking_list = []
        self.__user_name = user_name
        self.__display_name = display_name
        self.__gender = gender

    def booking_mate_by_name(self, platform, mate_name, day, start, end):
        if not isinstance(mate_name, str):
            return -1
        mate = platform.search_mate_by_name(mate_name)
        Platform.say(mate)
        input()
        mate.is_avaiable(day, start, end)

class Mate:
    def __init__(self, available, name) -> None:
        self.__available = False
        self.__name = name
        self.__time = None

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