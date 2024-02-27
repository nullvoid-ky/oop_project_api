from fastapi import APIRouter, Depends, HTTPException
from fastapi import status

from dependencies import create_token
from internal.auth import Auth
from models.account import AccountModel
from utils.response import Responses 
from models.message import MessageModel
from main import controller

responses = Responses()

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)

@router.post("/talk")
async def talking(body : MessageModel):
    try:
        controller.talk(body.sender_id, body.receiver_id, body.text)
        return Responses.success_response_status(status.HTTP_200_OK)
    except Exception as e:
        return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, e)
    

@router.get("/chat-history")
async def get_chat_history_by_id(sender_id: str, receiver_id: str):

    all_chat_data = controller.retrieve_chat_log(sender_id, receiver_id)
    
    if(len(all_chat_data) != 0):
        return all_chat_data
    else:
        return "No History"
    
@router.get("/chat-room")
async def get_chat_room_by_id(sender_id: str):

    all_chat_room = controller.retrieve_chat_room(sender_id)
    
    if(len(all_chat_room) != 0):
        return all_chat_room
    else:
        return "No History"