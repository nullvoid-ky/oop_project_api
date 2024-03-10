from internal.account import UserAccount

class Customer(UserAccount):
    def __init__(self, username: str, password: str, gender: str, location: str) -> None:
        super().__init__(username, password, gender, location)
    
    def get_account_details(self) -> dict:
        return {
            "id": str(self.id),
            "displayname": self.display_name,
            "username": self.username,
            "pic_url": self.pic_url,
            "role": "customer",
            "gender": self.gender,
            "location": self.location.capitalize(),
            "amount": self.amount,
            "timestamp": self._timestamp.strftime("%d/%m/%Y %H:%M:%S"),
            "age": self._age,
        }