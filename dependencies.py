from typing import Annotated
import jwt
import os
import uuid

from fastapi import Header, HTTPException

async def create_token(user_id: uuid = Annotated[str, "user_id"]) -> str:
    token: str = jwt.encode(payload={"user_id": str(user_id)}, key=os.getenv('JWT_SECRET'), algorithm="HS256")
    return token

async def verify_token(x_token: str = Header(...)) -> dict:
    try:
        payload: dict = jwt.decode(x_token, os.getenv('JWT_SECRET'), algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid token")