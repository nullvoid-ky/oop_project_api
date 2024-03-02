from internal.account import Account  
from argon2 import PasswordHasher 

ph = PasswordHasher()
    
async def register(username: str, password: str, role: str) -> dict | None:
    from app import controller
    account: Account = await controller.search_account_by_username(username)
    if account == None:
        hashed_password: str = ph.hash(password)
        if role == "customer":
            new_account: Account = await controller.add_customer(username, hashed_password)
        elif role == "mate":
            new_account: Account = await controller.add_mate(username, hashed_password)
        else:
            return None
        await controller.add_instance()
        return new_account.get_account_details()
    return None

async def login(username: str, password: str) -> dict | None:
    from app import controller
    account: Account = await controller.search_account_by_username(username)
    if account == None:
        return None
    try:
        ph.verify(account.password, password)
        return account.get_account_details()
    except:
        return None