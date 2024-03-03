from fastapi import APIRouter, Depends
from fastapi import status

from dependencies import verify_token
from models.booking import BookingModel
import utils.response as res   

router = APIRouter(
    prefix="/payment",
    tags=["payment"],
    dependencies=[Depends(verify_token)]
)

@router.post("/add-payment")
async def add_payment(body: BookingModel):
    from main import controller
    transaction: dict = await controller.add_payment(body.booking_id)
    if transaction == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in adding payment")
    return res.success_response_status(status.HTTP_201_addD, "Payment addd", transaction)