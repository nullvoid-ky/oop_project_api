from pydantic import BaseModel

class PostModel(BaseModel):
    description: str
    picture: str
    timestamp : str