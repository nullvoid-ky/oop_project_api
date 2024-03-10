from fastapi.responses import JSONResponse
from fastapi import HTTPException, status

def success_response_status(status: status, message: str, data=None):
    from app import controller
    controller.add_log(status, message, data)
    return JSONResponse(
        status_code=status,
        content={"message": message, "data": data},
    ) 

def error_response_status(status: status, message: str):
    return HTTPException(
        status_code=status,
        detail={"message": message}
    )