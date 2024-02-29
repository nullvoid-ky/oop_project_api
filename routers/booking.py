from fastapi import APIRouter, Depends, Body
from fastapi import status

from dependencies import verify_token
from models.booking import AddBookingModel
from internal.customer import Customer
from internal.mate import Mate

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
    
@router.post("/add-booking")
async def add_booking(body: AddBookingModel):
    from main import controller, responses
    customer: Customer = await controller.search_customer_by_id(Body.user_id)
    mate: Mate = await controller.search_mate_by_id(body.mate_id)
    result: dict = await controller.add_booking()
    if result:
        return responses.success_response_status(status=status.HTTP_201_CREATED, message="Booking addd", data=result)
    else:
        return responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Booking not addd")