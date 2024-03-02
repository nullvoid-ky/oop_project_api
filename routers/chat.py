from fastapi import APIRouter, Depends, Body
from fastapi import status

from internal.response import Responses 
from models.message import MessageModel, DeleteMessageModel
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
    msg = controller.talk(Body.user_id, body.receiver_id, body.text)
    if msg:
        return Responses.success_response_status(status.HTTP_200_OK, "Send message Success", {'id': str(msg.id), "text": msg.get_text(), "timestamp": msg.get_timestamp()})
    else:
        return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Send message Error")
    
@router.delete("/delete-message")
def talking(body: DeleteMessageModel):
    from app import controller
    msg_list = controller.delete_message(Body.user_id, body.receiver_id, body.message_id)
    if msg_list:
        return Responses.success_response_status(status.HTTP_200_OK, "Send message Success", [{'id': str(msg.id), "text": msg.get_text(), "timestamp": msg.get_timestamp()} for msg in msg_list])
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