from fastapi import APIRouter, Depends
from fastapi import status

from dependencies import verify_token
from models.payment import PaymentModel

router = APIRouter(
    prefix="/payment",
    tags=["payment"],
    dependencies=[Depends(verify_token)]
)

@router.post("/create-payment")
async def create_payment(body: PaymentModel):
    from main import responses, controller
    transaction: dict = await controller.create_payment(body.booking_id)
    if transaction == None:
        return responses.error_response_status(status.HTTP_404_NOT_FOUND, "Booking not found")
    return responses.success_response_status(status.HTTP_201_CREATED, "Payment created", transaction)