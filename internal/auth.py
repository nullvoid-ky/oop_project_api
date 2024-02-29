from internal.account import Account  
from argon2 import PasswordHasher 

ph = PasswordHasher()

class Auth:
    def __init__(self, username: str, password: str) -> None:
        self.__username = username
        self.__password = password
    
    async def register(self, role: str) -> dict | None:
        from main import controller
        account: Account = await controller.search_account_by_username(self.__username)
        if account == None:
            hashed_password: str = ph.hash(self.__password)
            if role == "customer":
                new_account: Account = await controller.add_customer(self.__username, hashed_password)
            elif role == "mate":
                new_account: Account = await controller.add_mate(self.__username, hashed_password)
            else:
                return None
            await controller.add_instance()
            return new_account.get_account_details()
        return None

    async def login(self) -> dict | None:
        from main import controller
        account: Account = await controller.search_account_by_username(self.__username)
        if account == None:
            return None
        try:
            ph.verify(account.password, self.__password)
            return account.get_account_details()
        except:
            return None