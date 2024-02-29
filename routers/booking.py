from fastapi import APIRouter, Depends
from fastapi import status
from dependencies import verify_token

router = APIRouter(
    prefix="/booking",
    tags=["booking"],
    dependencies=[Depends(verify_token)]
)

@router.get("/search-booking/{booking_id}")
async def search_booking(booking_id: str):
    from main import controller, responses
    result: dict = await controller.search_booking(booking_id)
    if result:
        return responses.success_response_status(status=status.HTTP_200_OK, message="Booking found", data=result)
    else:
        return responses.error_response_status(status.HTTP_404_NOT_FOUND, "Booking not found")