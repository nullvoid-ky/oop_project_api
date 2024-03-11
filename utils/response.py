from fastapi.responses import JSONResponse
from fastapi import HTTPException, status

def success_response_status(status: status, message: str, data=None):
    res = JSONResponse(
        status_code=status,
        content={"message": message, "data": data},
    ) 
    return res

def error_response_status(status: status, message: str):
    return HTTPException(
        status_code=status,
        detail={"message": message}
    )