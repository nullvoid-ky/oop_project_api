from fastapi import APIRouter, status, Depends, Body

from models.post import PostModel
from models.profile import EditUsernameModel, EditPicUrlModel
from models.mate import MateModel
from internal.booking import Booking
from internal.transaction import Transaction
from internal.account import Account
from internal.post import Post
from internal.chat_room_manager import ChatRoomManeger
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

@router.post("/add-booking", dependencies=[Depends(verify_customer)])
def add_booking(body: MateModel):
    from app import controller
    customer: Account = controller.search_customer_by_id(Body.user_id)
    if customer == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Customer not found")
    mate: Account = controller.search_mate_by_id(body.mate_id)  
    if mate == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    try:
        booking, transaction = controller.add_booking(customer, mate, body.date)
    except:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
    return res.success_response_status(status.HTTP_200_OK, "Booked Successfully", data={"booking": booking.get_booking_detail(), "transaction": transaction.get_transaction_details()})

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

@router.get("/get-user-data/{user_id}")
def get_user_data(user_id: str):
    from app import controller
    account: Account = controller.search_account_by_id(user_id)
    if account == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Account not found")
    return res.success_response_status(status.HTTP_200_OK, "Get User Data Success", data=account.get_account_details())

@router.delete("/delete-booking/{booking_id}", dependencies=[Depends(verify_customer)])
def delete_booking(booking_id: str):
    from app import controller
    booking: Booking = controller.search_booking_by_id(booking_id)
    account: Account = controller.search_account_by_id(Body.user_id)
    if booking == None or account == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Booking or Account not found")
    if controller.delete_booking(booking, account):
        return res.success_response_status(status.HTTP_200_OK, "Delete Booking Success")
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in delete booking")

@router.post("/add-chat-room", dependencies=[Depends(verify_customer)])
def add_chat_room(body: AddChatRoomModel):
    from app import controller
    account_1: Account = controller.search_account_by_id(Body.user_id)
    account_2: Account = controller.search_account_by_id(body.receiver_id)
    chat_room: ChatRoomManeger = controller.add_chat_room(account_1, account_2)
    if chat_room == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Account not found")
    return res.success_response_status(status.HTTP_200_OK, "Add Chat Room Success", data=chat_room.get_chat_room_details())

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

    
@router.get("/get-leaderboard")
def get_leaderboard():
    from app import controller
    mate_list : list = controller.get_leaderboard()
    my_list = []
    for mate in mate_list:
        my_list.append(mate.get_account_details)
    if len(my_list):
        return res.success_response_status(status.HTTP_200_OK, "Get Leaderboard Success", data=my_list)
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Account not found")
