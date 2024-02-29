from typing import Annotated
import jwt
import os
from dotenv import load_dotenv

from fastapi import Header, HTTPException, Body

load_dotenv()

def create_token(user_id: str = Annotated[str, "user_id"]) -> str:
    token: str = jwt.encode(payload={ "user_id": user_id }, key=os.environ['JWT_SECRET'], algorithm="HS256")
    return token

def verify_token(x_token: str = Header(...)) -> dict:
    try:
        payload: dict = jwt.decode(x_token, os.getenv('JWT_SECRET'), algorithms=["HS256"])
        Body.user_id = payload["user_id"]
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid token")