from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, payment, booking, chat
from internal.controller import Controller
from utils.response import Responses

responses = Responses()
controller = Controller()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

controller = Controller()

app.include_router(
    auth.router,
    prefix="/api",
    tags=["auth"]
)
app.include_router(
    chat.router,
    prefix="/api",
    tags=["chat"]
)
app.include_router(
    payment.router,
    prefix="/api",
    tags=["payment"]
)
app.include_router(
    booking.router,
    prefix="/api",
    tags=["booking"]
)