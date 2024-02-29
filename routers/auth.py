from fastapi import APIRouter
from fastapi import status

from dependencies import create_token
from internal.auth import Auth
from models.register import RegisterModel
from models.login import LoginModel

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/login")
async def login(body: LoginModel):
    from main import responses
    auth: Auth = Auth(body.username, body.password)
    account: dict = await auth.login()
    if account:
        token: str = create_token(str(account["id"]))
        return responses.success_response_status(status=status.HTTP_200_OK, message="Login successful", data={"token": token, "username": account["username"], "pic_url": account["pic_url"]})
    else:
        return responses.error_response_status(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

@router.post("/register")
async def register(body: RegisterModel):
    from main import responses
    auth: Auth = Auth(body.username, body.password)
    account: dict = await auth.register(body.role)
    if account:
        token: str = create_token(str(account["id"]))
        return responses.success_response_status(status=status.HTTP_201_CREATED, message="Account created", data={"token": token, "username": account["username"], "pic_url": account["pic_url"]})
    else:
        return responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Account already exists")