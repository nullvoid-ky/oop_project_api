from fastapi import APIRouter
from fastapi import status

from dependencies import create_token
from models.register import RegisterModel
from models.login import LoginModel
import utils.auth as auth
import utils.response as res
from internal.account import Account
from internal.customer import Customer
from internal.mate import Mate

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/login")
async def login(body: LoginModel):
    account: dict = await auth.login(body.username, body.password)
    if account:
        token: str = create_token(str(account["id"]), "customer" if isinstance(account, Customer) else "mate")
        return res.success_response_status(status=status.HTTP_200_OK, message="Login successful", data={"token": token, "id": account["id"], "username": account["username"], "pic_url": account["pic_url"]})
    else:
        return res.error_response_status(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

@router.post("/register")
async def register(body: RegisterModel):
    account: dict = await auth.register(body.username, body.password, body.role)
    if account:
        token: str = create_token(str(account["id"]), body.role)
        return res.success_response_status(status=status.HTTP_201_CREATED, message="Account added", data={"token": token, "id": account["id"], "username": account["username"], "pic_url": account["pic_url"]})
    else:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Account already exists")