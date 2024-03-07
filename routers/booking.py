from fastapi import APIRouter, Depends, Body
from fastapi import status
from dependencies import verify_token
from internal.booking import Booking
import utils.response as res

router = APIRouter(
    prefix="/booking",
    tags=["booking"],
    dependencies=[Depends(verify_token)]
)

@router.get("/search-booking/{booking_id}")
def search_booking(booking_id: str):
    from app import controller
    result: Booking = controller.search_booking_by_id(booking_id)
    if result:
        return res.success_response_status(status.HTTP_200_OK, "Booking found", data=result.get_booking_detail())
    else:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Booking not found")