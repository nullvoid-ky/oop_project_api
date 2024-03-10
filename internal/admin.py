from internal.account import AllAccount

class Admin(AllAccount):
    def __init__(self):
        username : str = "admin"
        password : str = "admin"
        super().__init__(username, password)
    
    def get_account_details(self) -> dict:
        return {
            "id": str(self.id),
            "username": self.username,
            "displayname":self.display_name,
            "pic_url": self.pic_url,
            "role": "admin",
            "gender":self.gender,
            "location": self.location,
            "timestamp": self.timestamp.strftime("%d/%m/%Y %H:%M:%S")
        }