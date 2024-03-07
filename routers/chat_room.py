from typing import Annotated

from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect

from dependencies import verify_token_websocket
from internal.chat_room_manager import ChatRoomManeger
from internal.account import Account

router = APIRouter(
    prefix="/chat-room",
    tags=["chat-room"],
)

@router.websocket("/{chat_room_id}")
async def websocket_endpoint(websocket: WebSocket, chat_room_id: str, user_id: Annotated[str, Depends(verify_token_websocket)]):
    from app import controller
    account: Account = controller.search_account_by_id(user_id)
    manager: ChatRoomManeger = controller.search_chat_room_by_id(chat_room_id)
    await manager.connect(websocket, account)
    try:
        while True:
            data: str = await websocket.receive_text()
            await manager.add_message(data, account)
            await manager.broadcast(f"Message text was: {data} from user {user_id}")
    except WebSocketDisconnect:
        manager.disconnect(websocket, account)
        await manager.broadcast(f"User {user_id} is offline")