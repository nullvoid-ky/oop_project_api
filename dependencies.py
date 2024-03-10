from fastapi import Header, HTTPException, Body, Depends, WebSocketException, WebSocket, status

from typing import Annotated
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

def create_token(user_id: str = Annotated[str, "user_id"], role: str = Annotated[str, "role"]) -> str:
    token: str = jwt.encode(payload={ "user_id": user_id, "role": role }, key=os.environ['JWT_SECRET'], algorithm="HS256")
    return token

def verify_token_websocket(x_token: str = Header(...)) -> str:
    try:
        payload: dict = jwt.decode(x_token, os.getenv('JWT_SECRET'), algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION, reason="Token has expired")
    except jwt.InvalidTokenError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION, reason="Invalid token")

def verify_token(x_token: str = Header(...)) -> dict:
    try:
        payload: dict = jwt.decode(x_token, os.getenv('JWT_SECRET'), algorithms=["HS256"])
        Body.user_id = payload["user_id"]
        Body.role = payload["role"]
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=400, detail="Invalid token")
    
def verify_customer(payload: dict = Depends(verify_token)):
    if "role" not in payload:
        raise HTTPException(status_code=400, detail="Role not found in token")
    if payload["role"] != "customer":
        raise HTTPException(status_code=403, detail="Only customers are allowed")
    return payload

def verify_mate(payload: dict = Depends(verify_token)):
    if "role" not in payload:
        raise HTTPException(status_code=400, detail="Role not found in token")
    if payload["role"] != "mate":
        raise HTTPException(status_code=403, detail="Only mates are allowed")
    return payload

def verify_admin(payload: dict = Depends(verify_token)):
    if "role" not in payload:
        raise HTTPException(status_code=400, detail="Role not found in token")
    if payload["role"] != "admin":
        raise HTTPException(status_code=403, detail="Only admins are allowed")
    return payload