from pydantic import BaseModel

class AccountModel(BaseModel):
    age: int
    location: str