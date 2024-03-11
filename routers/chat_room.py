from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from dependencies import verify_token_websocket
from internal.chat_room_manager import ChatRoomManeger
from internal.account import UserAccount

router = APIRouter(
    prefix="/chat-room",
    tags=["chat-room"],
)

@router.websocket("/{chat_room_id}/{token}")
async def websocket_endpoint(websocket: WebSocket, chat_room_id: str, token: str):
    from app import controller
    from internal.message import Message
    user_id = verify_token_websocket(token)
    account: UserAccount = controller.search_account_by_id(user_id)
    manager: ChatRoomManeger = controller.search_chat_room_by_id(chat_room_id)
    await manager.connect(websocket, account)
    try:
        while True:
            data: str = await websocket.receive_text()
            msg: Message = await manager.add_message(data, account)
            await manager.broadcast(str(msg.get_message_details()))
    except WebSocketDisconnect:
        manager.disconnect(websocket, account)
        await manager.broadcast(f"User {user_id} is offline")