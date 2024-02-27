from pydantic import BaseModel

class AccountModel(BaseModel):
    username: str
    password: str
