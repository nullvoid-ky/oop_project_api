from internal.account import UserAccount, Account  
from internal.admin import Admin
from argon2 import PasswordHasher 
from models.mate import Date

ph = PasswordHasher()
    
def register(username: str, password: str, role: str, gender: str, location : str= "Bangkok") -> dict | None:
    from app import controller
    return controller.register(username, password, role, gender, location)

def login(username: str, password: str) -> dict | None:
    from app import controller
    return controller.login(username, password)