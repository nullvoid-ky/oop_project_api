from pydantic import BaseModel

class MessageModel(BaseModel):
    receiver_id: str
    text: str

class DeleteMessageModel(BaseModel):
    receiver_id: str
    message_id: str

class EditMessageModel(BaseModel):
    chat_room_id: str
    message_id: str
    new_text: str