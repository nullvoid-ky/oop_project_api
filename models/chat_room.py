from pydantic import BaseModel

class DeleteChatRoomModel(BaseModel):
    receiver_id: str

class AddChatRoomModel(BaseModel):
    mate_id: str