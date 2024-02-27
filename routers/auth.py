from fastapi import APIRouter, Depends, HTTPException
from fastapi import status

from ..dependencies import create_token
from ..internal.auth import Auth
from ..models.account import AccountModel
from ..utils.response import Responses 

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/login")
async def login(body: AccountModel):
    auth: Auth = Auth(body.username, body.password)
    account: dict = await auth.login()
    token: str = await create_token(account["id"])
    if token:
        return Responses.success_response_status(status.HTTP_200_OK, "Login successful", {"token": token, "username": account["username"], "pic_url": account["pic_url"]})
    else:
        return Responses.error_response_status(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")
    
@router.post("/register")
async def register(body: AccountModel):
    auth: Auth = Auth(body.username, body.password)
    account: dict = await auth.register()
    token: str = await create_token(account["id"])
    if account:
        return Responses.success_response_status(status.HTTP_201_CREATED, "Account created", {"token": token, "username": account["username"], "pic_url": account["pic_url"]})
    else:
        return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Account already exists")