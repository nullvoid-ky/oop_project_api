from internal.account import Account  
import bcrypt 

class Auth:
    def __init__(self, username: str, password: str) -> None:
        self.__user = username
        self.__password = password
    
    async def register(self) -> dict | None:
        from main import controller
        account: Account = await controller.get_account_by_username(self.__user)
        if account == None:
            hashed_password = bcrypt.hashpw(self.__password.encode('utf-8'), bcrypt.gensalt())
            new_account: Account = controller.add_account(self.__user, str(hashed_password))
            return new_account.get_account_details()
        return None

    async def login(self):
        from main import controller
        account: Account = await controller.get_account_by_username(self.__user)
        if account == None:
            return None
        if bcrypt.checkpw(self.__password.encode('utf-8'), account.password):
            return account.get_account_details()
        return None