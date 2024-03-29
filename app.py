from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, chat, chat_room, controller, mate
from internal.controller import Controller

app = FastAPI(openapi_prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(
    auth.router,
    tags=["auth"]
)
app.include_router(
    chat.router,
    tags=["chat"]
)
app.include_router(
    controller.router, 
    tags=["controller"]
)
app.include_router(
    mate.router,
    tags=["mate"]
)
app.include_router(
    chat_room.router,
    tags=["chat-room"]
)

controller = Controller()
controller.add_instance()