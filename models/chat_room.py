from pydantic import BaseModel

class DeleteChatRoomModel(BaseModel):
    receiver_id: str

class AddChatRoomModel(BaseModel):
    sender_id: str
    receiver_id: str