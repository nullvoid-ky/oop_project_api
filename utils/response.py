from fastapi.responses import JSONResponse
from fastapi import HTTPException

class Responses:
    @staticmethod
    def success_response_status(status: int, message: str, data):
        return JSONResponse(
            status_code=status,
            content={"message": message, "data" : data},
        )
    @staticmethod
    def error_response_status( status: int, message: str):
        return HTTPException(
            status_code=status,
            detail={"message": message}
        )