from datetime import datetime
from internal.account import UserAccount
class Log:
    def __init__(self, success, actor, action, item, target, msg) -> None:
        self.__success : True | False = success
        self.__actor = actor
        self.__action = action
        self.__item = item
        self.__target = target
        self.__msg = msg
        self.__timestamp =  datetime.now()

        @property
        def success(self):
            return self.__success
        @property
        def actor(self):
            return self.__actor
        @property
        def action(self):
            return self.__action
        @property
        def item(self):
            return self.__item
        @property
        def target(self):
            return self.__target
        @property
        def msg(self):
            return self.__msg
        @property
        def timestamp(self):
            return self.__timestamp
        
        def get_log_details(self):
            if isinstance(item, str):
                return {
                    "success" : self.__success,
                    "actor" : self.__actor.get_account_details() if not isinstance(self.__actor , UserAccount) else "?",
                    "action" : self.__action,
                    "item" : self.__item,
                    "target" : self.__target.get_account_details() if not isinstance(self.__target , UserAccount)else "?",
                    "msg" : self.__msg,
                    "timestamp" : self.__timestam.strftime("%d/%m/%Y %H:%M")
                }
            else:
                return {
                    "success" : self.__success, 
                    "actor" : self.__actor.get_account_details() if not isinstance(self.__actor , UserAccount) else "?",
                    "action" : self.__action,
                    "item" : str(type(self.__item)),
                    "target" : self.__target.get_account_details() if not isinstance(self.__target , UserAccount)else "?",
                    "msg" : self.__msg,
                    "timestamp" : self.__timestam.strftime("%d/%m/%Y %H:%M")
                }

            