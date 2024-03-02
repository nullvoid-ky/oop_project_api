from pydantic import BaseModel

class DeleteChatRoomModel(BaseModel):
    receiver_id: str