from pydantic import BaseModel

class EditUsernameModel(BaseModel):
    username: str

class EditPicUrlModel(BaseModel):
    url: str