from pydantic import BaseModel

class MessageModel(BaseModel):
    sender_id: str
    receiver_id: str
    text: str
