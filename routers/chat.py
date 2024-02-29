from fastapi import APIRouter, Depends, Body
from fastapi import status

from internal.response import Responses 
from models.message import MessageModel
from dependencies import verify_token

responses = Responses()

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    dependencies=[Depends(verify_token)]
)

@router.post("/talk")
def talking(body: MessageModel):
    from app import controller
    respond = controller.talk(Body.user_id, body.receiver_id, body.text)
    if respond:
        return Responses.success_response_status(status.HTTP_200_OK, "Send message Success", None)
    else:
        return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Send message Error")
    

@router.get("/chat-history/{receiver_id}")
def get_chat_history_by_id(receiver_id: str):
    from app import controller
    all_chat_data = controller.retrieve_chat_log(Body.user_id, receiver_id)
    
    if len(all_chat_data) != 0:
        return all_chat_data
    else:
        return "No History"
    
@router.get("/chat-room")
def get_chat_room_by_id():
    from app import controller
    all_chat_room = controller.retrieve_chat_room(Body.user_id)
    if len(all_chat_room) != 0:
        return all_chat_room
    else:
        return "No History"