from pydantic import BaseModel

class MessageModel(BaseModel):
    receiver_id: str
    text: str
