from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dependencies import create_token, verify_token
from routers import auth, payment
from internal.controller import Controller
from internal.response import Responses
from utils.create_instance import create_instance

responses = Responses()
controller = Controller()

create_instance()

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
app.include_router(
    payment.router,
    prefix="/api",
    tags=["payment"]
)