from internal.controller import Controller
from internal.account import Account  
import bcrypt 

controller = Controller() 

class Auth:
    def __init__(self, username: str, password: str) -> None:
        self.__user = username
        self.__password = password
    
    def register(self) -> dict | None:
        account: Account = controller.get_account_by_username(self.__user)
        if account == None:
            return None
        hashed_password = bcrypt.hashpw(self.__password.encode('utf-8'), bcrypt.gensalt())
        controller.add_account(self.__user, hashed_password)
        return account.get_account_details()

    def login(self):
        account: Account = controller.get_account_by_username(self.__user)
        if account == None:
            return None
        if bcrypt.checkpw(self.__password.encode('utf-8'), account.password):
            return account.get_account_details()
        return None