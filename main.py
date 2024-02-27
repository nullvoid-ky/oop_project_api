from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dependencies import create_token, verify_token
from routers import auth
from internal.controller import Controller
from models.message import MessageModel

controller = Controller()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    auth.router,
    prefix="/api",
    tags=["auth"]
)

controller = Controller()

@app.post("/talk")
async def talking(message : MessageModel):
    controller.talk(message.sender_id, message.receiver_id, message.text)
    return "Sending msg success!!!"

@app.get("/chat_history")
async def get_chat_history_by_customer_id(sender_id: str, receiver_id: str):

    all_chat_data = controller.retrieve_chat_log(sender_id, receiver_id)
    
    if(len(all_chat_data) != 0):
        return all_chat_data
    else:
        return "No History"