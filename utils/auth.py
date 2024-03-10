from internal.account import UserAccount, Account  
from internal.admin import Admin
from argon2 import PasswordHasher 
from models.mate import Date

ph = PasswordHasher()
    
def register(username: str, password: str, role: str, gender: str, location : str= "Bangkok") -> dict | None:
    from app import controller
    account: Account = controller.search_account_by_username(username)
    if account == None and username != "admin":
        hashed_password: str = ph.hash(password)
        if role == "customer":
            new_account: UserAccount = controller.add_customer(username, hashed_password, gender, location)
            if gender == "male":
                new_account.add_pic_url("../img/customer_male.svg")
            else:
                new_account.add_pic_url("../img/customer_female.svg")
        elif role == "mate":
            new_account: UserAccount = controller.add_mate(username, hashed_password, gender, location)
            if gender == "male":
                new_account.add_pic_url("../img/mate_male.svg")
            else:
                new_account.add_pic_url("../img/mate_female.svg")
        else:
            return None
        # mate = controller.search_account_by_username("Mate2")
        # booking = controller.add_booking(new_account, mate, Date(year=2024, month=3, day=4))
        return new_account.get_account_details()
    return None

def login(username: str, password: str) -> dict | None:
    from app import controller
    account: Account = controller.search_account_by_username(username)
    if account == None:
        return None
    # return account.get_account_details()
    try:
        # if isinstance(account, Admin):
        #     ph.verify("admin", password)
        #     return account.get_account_details()
        ph.verify(account.password, password)
        return account.get_account_details()
    except:
        return None