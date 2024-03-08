from fastapi import APIRouter, status, Depends, Body
from typing import Union, Tuple

from models.post import PostModel
from models.profile import EditDisplayNameModel, EditPicUrlModel
import utils.response as res
from models.mate import MateModel, SearchMateModel
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

@router.post("/search-mates")
def search_mate_by_condition(body: SearchMateModel):
    from app import controller
    print(body.name, body.location, body.gender, body.age)
    mate_list = controller.search_mate_by_condition(body.name, body.location, body.gender, body.age)
    print(mate_list)
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
    booking_list: list = controller.get_booking(customer)
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
    deleted_booking: Union[Tuple[Booking, Transaction], Booking, None] = controller.delete_booking(booking, account)
    if isinstance(deleted_booking, tuple):
        return res.success_response_status(status.HTTP_200_OK, "Delete Booking Success", data={"booking": deleted_booking[0].get_booking_detail(), "transaction": deleted_booking[1].get_transaction_details()})
    elif isinstance(deleted_booking, Booking):
        return res.success_response_status(status.HTTP_200_OK, "Delete Booking Success", data=deleted_booking.get_booking_detail())
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

@router.put("/edit-displayname")
def edit_display_name(body: EditDisplayNameModel):
    from app import controller
    account: Account = controller.edit_display_name(Body.user_id, body.display_name)
    if account:
        return res.success_response_status(status.HTTP_200_OK, "Edit displayname Success",  data=account.get_account_details())
    else:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Edit displayname Error")
    
@router.post("/edit-pic-url")
def edit_pic_url(body: EditPicUrlModel):
    from app import controller
    account: Account = controller.edit_pic_url(Body.user_id, body.url)
    if account:
        return res.success_response_status(status.HTTP_200_OK, "Edit pic url Success",  data=account.get_account_details())
    else:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Send pic url Error")
    
@router.get("/get-leaderboard")
def get_leaderboard():
    rank = 1
    from app import controller
    mate_list : list = controller.get_leaderboard()
    my_list = []
    for mate in mate_list:
        my_list.append(mate)
    send_data = [{'account_detail' : acc.get_mate_details()} for acc in my_list]
    for data in send_data:
        data["account_detail"]["rank"] = rank
    if len(my_list):
        return res.success_response_status(status.HTTP_200_OK, "Get Leaderboard Success", data=send_data)
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Account not found")
