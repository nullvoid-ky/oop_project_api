from internal.account import Account, AllAccount  
from internal.admin import Admin
from argon2 import PasswordHasher 
from models.mate import Date

ph = PasswordHasher()
    
def register(username: str, password: str, role: str, gender: str, location: str) -> dict | None:
    from app import controller
    account: Account = controller.search_account_by_username(username)
    if account == None:
        hashed_password: str = ph.hash(password)
        if role == "customer":
            new_account: Account = controller.add_customer(username, hashed_password, gender, location)
        elif role == "mate":
            new_account: Account = controller.add_mate(username, hashed_password, gender, location)
        else:
            return None
        # mate = controller.search_account_by_username("Mate2")
        # booking = controller.add_booking(new_account, mate, Date(year=2024, month=3, day=4))
        return new_account.get_account_details()
    return None

def login(username: str, password: str) -> dict | None:
    from app import controller
    account: AllAccount = controller.search_account_by_username(username)
    if account == None:
        return None
    return account.get_account_details()
    # try:
    #     # if isinstance(account, Admin):
    #         # ph.verify("admin", password)
    #         # return account.get_account_details()
    #     ph.verify(account.password, password)
    #     return account.get_account_details()
    # except:
    #     return None