from fastapi import Header, Depends

from typing import Annotated

def create_token(user_id: str = Annotated[str, "user_id"], role: str = Annotated[str, "role"]) -> str:
    from app import controller
    return controller.create_token(user_id, role)

def verify_token_websocket(x_token: str = Header(...)) -> str:
    from app import controller
    return controller.verify_token_websocket(x_token)

def verify_token(x_token: str = Header(...)) -> dict:
    from app import controller
    return controller.verify_token(x_token)
    
def verify_customer(payload: dict = Depends(verify_token)):
    from app import controller
    return controller.verify_customer(payload)

def verify_mate(payload: dict = Depends(verify_token)):
    from app import controller
    return controller.verify_mate(payload)

def verify_admin(payload: dict = Depends(verify_token)):
    from app import controller
    return controller.verify_admin(payload)