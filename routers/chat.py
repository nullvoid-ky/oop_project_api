from fastapi import APIRouter, Depends, Body
from fastapi import status

from models.message import MessageModel, EditMessageModel
from models.chat_room import DeleteChatRoomModel
from dependencies import verify_token
import utils.response as res

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    dependencies=[Depends(verify_token)]
)
    
# @router.delete("/delete-message")
# def delete_message(body: DeleteMessageModel):
#     from app import controller
#     msg_list = controller.delete_message(Body.user_id, body.receiver_id, body.message_id)
#     if isinstance(msg_list, list):
#         return res.success_response_status(status.HTTP_200_OK, "Delete message Success", [{'id': str(msg.id), "text": msg.get_text(), "timestamp": msg.get_timestamp(), "is_edit": msg.is_edit} for msg in msg_list])
#     else:
#         return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Send message Error")
    
@router.put("/edit-message/{chat_room_id}")
def edit_message(body: EditMessageModel):
    from app import controller
    chat_room = controller.search_chat_room_by_id(body.chat_room_id)
    if chat_room is None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Chat Room not found")
    message = chat_room.search_message_by_id(body.message_id)
    if message is None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Message not found")
    message.set_text(body.new_text)
    return res.success_response_status(status.HTTP_200_OK, "Edit message Success", message.get_message_details())

@router.get("/get-chat-history/{chat_room_id}")
def get_chat_history_by_id(chat_room_id: str):
    from app import controller
    chat_list: list = controller.get_chat_history_by_id(chat_room_id)
    if chat_list:
        return res.success_response_status(status.HTTP_200_OK, "Get Chat History Success", data=[c.get_message_details() for c in chat_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "No Chat History")
    
@router.get("/get-chat-room")
def get_chat_rooms():
    from app import controller
    account = controller.search_account_by_id(Body.user_id)
    if account is None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "UserAccount not found")
    # chat_list = controller.get_chat_list(account)
    chat_list = controller.get_receiver_chat_room_detail(account)
    if chat_list is None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "No Chat Room")
    return res.success_response_status(status.HTTP_200_OK, "Get Chat Room Success", chat_list)
    
# @router.delete("/delete-chat-room")
# def delete_chat_room(body: DeleteChatRoomModel):
#     from app import controller
#     chat = controller.delete_chat_room(Body.user_id, body.receiver_id)
#     if isinstance(chat, list):
#         return res.success_response_status(status.HTTP_200_OK, "Delete Chat Room Success", chat)
#     else:
#         return res.error_response_status(status.HTTP_400_BAD_REQUEST, "No Chat Room To Delete")