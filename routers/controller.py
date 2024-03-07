from fastapi import APIRouter, status, Depends, Body

from internal.booking import Booking
from internal.transaction import Transaction
from internal.account import Account
from internal.post import Post
from internal.chat_room_manager import ChatRoomManeger
from models.controller import ReviewModel
from models.post import PostModel
from models.mate import MateModel
from models.booking import BookingModel
from models.chat_room import AddChatRoomModel
import utils.response as res
from dependencies import verify_token, verify_customer, verify_mate

router = APIRouter(
    prefix="/controller",
    tags=["controller"],
    dependencies=[Depends(verify_token)]
)

@router.post("/add-review", dependencies=[Depends(verify_customer)])
def add_review(body: ReviewModel):
    from app import controller
    review = controller.add_review_mate(Body.user_id, body.mate_id, body.message, body.star)
    if isinstance(review, None):
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
    return res.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=review.get_review_details())

@router.post("/add-booking", dependencies=[Depends(verify_customer)])
def add_booking(body: MateModel):
    from app import controller
    customer: Account = controller.search_customer_by_id(Body.user_id)
    if customer == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Customer not found")
    mate: Account = controller.search_mate_by_id(body.mate_id)  
    if mate == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    booking: Booking = controller.add_booking(customer, mate, body.date)
    if isinstance(booking, Booking):
        return res.success_response_status(status.HTTP_200_OK, "Booked Successfully", data=booking.get_booking_detail())
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.post("/pay", dependencies=[Depends(verify_customer)])
def pay(body: BookingModel):
    from app import controller
    transaction: Transaction = controller.pay(body.booking_id)
    if isinstance(transaction, Transaction):
        return res.success_response_status(status.HTTP_201_CREATED, "Payment added", data=transaction.get_transaction_details())
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in adding payment")

@router.get("/get-mates")
def get_mates():
    from app import controller
    mate_list = controller.get_mates()
    if isinstance(mate_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Mate Success", data=[{'account_detail' : acc.get_account_details()} for acc in mate_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in add mate")

@router.post("/add-post", dependencies=[Depends(verify_mate)])
def add_post(body: PostModel):
    from app import controller
    post: Post = controller.add_post(body.description, body.picture)
    if post == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in add post")
    return res.success_response_status(status.HTTP_200_OK, "Add Post Success", data=post.get_post_details())

@router.get("/get-booking", dependencies=[Depends(verify_customer)])
def get_booking():
    from app import controller
    customer: Account = controller.search_customer_by_id(Body.user_id)
    booking_list = controller.get_booking(customer)
    if isinstance(booking_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Booking Success", data=[booking.get_booking_detail() for booking in booking_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in get booking")

@router.get("/get-user-profile")
def get_profile():
    from app import controller
    account: Account = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Account not found")
    return res.success_response_status(status.HTTP_200_OK, "Get Profile Success", data=account.get_account_details())

@router.delete("/delete-booking/{booking_id}", dependencies=[Depends(verify_customer)])
def delete_booking(booking_id: str):
    from app import controller
    booking: Booking = controller.search_booking_by_id(booking_id)
    if booking == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Booking not found")
    if controller.delete_booking(booking_id):
        return res.success_response_status(status.HTTP_200_OK, "Delete Booking Success")
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in delete booking")

@router.post("/add-chat-room", dependencies=[Depends(verify_customer)])
def add_chat_room(body: AddChatRoomModel):
    from app import controller
    chat_room: ChatRoomManeger = controller.add_chat_room(Body.user_id, body.receiver_id)
    if chat_room == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Account not found")
    return res.success_response_status(status.HTTP_200_OK, "Add Chat Room Success", data=chat_room.get_chat_room_details())