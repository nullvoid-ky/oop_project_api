from internal.account import Account

class Admin(Account):
    def __init__(self):
        username :str = "admin"
        password : str = "admin"
        gender : str = "admin"
        location : str = "admin"
        super().__init__(username, password, gender, location)