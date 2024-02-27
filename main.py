from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dependencies import create_token, verify_token
from routers import auth
from internal.controller import Controller

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