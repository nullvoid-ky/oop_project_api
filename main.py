from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from internal.controller import Controller
# from .dependencies import verify_token
from .routers import *

controller = Controller()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# app.include_router(
#     auth.router,
#     prefix="/api",
#     tags=["auth"]
# )

app.include_router(
    controller.router,
    prefix="/controller",
    tags=["controller"]
)

@app.get("/")
async def read_root():
  return {"message": "This is API for Athletix website."}