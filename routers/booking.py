from fastapi import APIRouter, Depends, Body
from fastapi import status

from dependencies import verify_token
from models.booking import AddBookingModel
from internal.customer import Customer
from internal.mate import Mate
from internal.booking import Booking

router = APIRouter(
    prefix="/booking",
    tags=["booking"],
    dependencies=[Depends(verify_token)]
)

@router.get("/search-booking/{booking_id}")
async def search_booking(booking_id: str):
    from app import controller, responses
    result: dict = await controller.search_booking(booking_id)
    if result:
        return responses.success_response_status(status=status.HTTP_200_OK, message="Booking found", data=result)
    else:
        return responses.error_response_status(status.HTTP_404_NOT_FOUND, "Booking not found")
    
@router.post("/add-booking")
async def add_booking(body: AddBookingModel):
    from app import controller, responses
    customer: Customer = await controller.search_customer_by_id(Body.user_id)
    if customer == None:
        return responses.error_response_status(status.HTTP_404_NOT_FOUND, "Customer not found")
    mate: Mate = await controller.search_mate_by_id(body.mate_id)
    if mate == None:
        return responses.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    result: Booking = await controller.add_booking(customer, mate, body.amount)
    return responses.success_response_status(status=status.HTTP_201_CREATED, message="Booking added", data=result.get_booking_detail())