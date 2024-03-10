from pydantic import BaseModel

class PostModel(BaseModel):
    description: str
    pic_url: str