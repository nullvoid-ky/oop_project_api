from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dependencies import create_token, verify_token
from routers import auth, chat
from internal.controller import Controller
from internal.account import Account
from internal.chat import Chat

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

controller = Controller()

customer_acc = Account("Kan", "1234")
print(customer_acc.id)
mate_acc = Account("Gan", "1234")
print(mate_acc.id)
# controller.__account_list = [
#     customer_acc,
#     mate_acc
# ]

controller.add_account_instance(customer_acc)
controller.add_account_instance(mate_acc)

controller.add_chat_room(Chat(customer_acc, mate_acc))

app.include_router(
    auth.router,
    prefix="/api",
    tags=["auth"]
)

app.include_router(
    chat.router,
    prefix="/chat",
    tags=["chat"]
)