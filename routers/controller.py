from fastapi import APIRouter, status, Depends, Body

from models.controller import ReviewModel
from dependencies import verify_token 
import utils.response as res
from models.mate import MateModel
from internal.booking import Booking
from internal.transaction import Transaction
from models.booking import BookingModel

router = APIRouter(
    prefix="/controller",
    tags=["controller"],
    dependencies=[Depends(verify_token)]
)

@router.post("/add-review")
def add_review(body: ReviewModel):
    from app import controller
    review = controller.add_review_mate(Body.user_id, body.mate_id, body.message, body.star)
    if isinstance(review, None):
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
    return res.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=review.get_review_details())

@router.post("/book-mate")
async def book_mate(body: MateModel):
    from app import controller
    booking: Booking = await controller.book_mate(Body.user_id, body.mate_id)
    if isinstance(booking, Booking):
        return res.success_response_status(status.HTTP_200_OK, "Booked Successfully", data=booking.get_booking_detail())
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.post("/add-payment")
def add_payment(body: BookingModel):
    from app import controller
    transaction: Transaction = controller.add_payment(body.booking_id)
    if isinstance(transaction, Transaction):
        return res.success_response_status(status.HTTP_201_CREATED, "Payment added", data=transaction.get_transaction_details())
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in adding payment")