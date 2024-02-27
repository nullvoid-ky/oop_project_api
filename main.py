from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, payment
from internal.controller import Controller
from internal.response import Responses

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