from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import auth, payment, booking, chat
from internal.controller import Controller

controller = Controller()

app = FastAPI(openapi_prefix="/api")
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
    tags=["auth"]
)
app.include_router(
    chat.router,
    tags=["chat"]
)
app.include_router(
    payment.router,
    tags=["payment"]
)
app.include_router(
    booking.router,
    tags=["booking"]
)