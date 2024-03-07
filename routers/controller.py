from fastapi import APIRouter, status, Depends, Body

from models.controller import ReviewModel
from models.post import PostModel
from models.profile import EditUsernameModel, EditPicUrlModel
import utils.response as res
from models.mate import MateModel
from internal.booking import Booking
from internal.transaction import Transaction
from internal.account import Account
from internal.post import Post
from models.booking import BookingModel
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

@router.put("/edit-username")
def edit_message(body: EditUsernameModel):
    from app import controller
    account: Account = controller.edit_username(Body.user_id, body.username)
    if account:
        return res.success_response_status(status.HTTP_200_OK, "Edit username Success",  data=account.get_account_details())
    else:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Edit username Error")
    
@router.put("/edit-pic-url")
def edit_message(body: EditPicUrlModel):
    from app import controller
    account: Account = controller.edit_pic_url(Body.user_id, body.url)
    if account:
        return res.success_response_status(status.HTTP_200_OK, "Edit pic url Success",  data=account.get_account_details())
    else:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Send pic url Error")