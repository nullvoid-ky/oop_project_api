from pydantic import BaseModel

class MessageModel(BaseModel):
    receiver_id: str
    text: str

class DeleteMessageModel(BaseModel):
    receiver_id: str
    message_id: str