from fastapi import APIRouter, Depends, Body
from fastapi import status

from dependencies import verify_token
from models.booking import BookingModel

router = APIRouter(
    prefix="/payment",
    tags=["payment"],
    dependencies=[Depends(verify_token)]
)

@router.post("/add-payment")
async def add_payment(body: BookingModel):
    # print("body : ", Body.user_id)
    from main import responses, controller
    transaction: dict = await controller.add_payment(body.booking_id)
    if transaction == None:
        return responses.error_response_status(status.HTTP_404_NOT_FOUND, "Booking not found")
    return responses.success_response_status(status.HTTP_201_addD, "Payment addd", transaction)