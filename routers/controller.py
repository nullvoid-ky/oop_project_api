from fastapi import APIRouter, status, Depends, Body
from typing import Union, Tuple

from models.post import PostModel
from models.profile import EditDisplayNameModel, EditPicUrlModel, EditMoneyModel, EditAgeModel, EditLocationModel
from models.mate import MateModel, SearchMateModel
from internal.booking import Booking
from internal.transaction import Transaction
from internal.account import UserAccount, Account
from internal.post import Post
from internal.chat_room_manager import ChatRoomManeger
from internal.mate import Mate
from models.post import PostModel
from models.mate import MateModel
from models.booking import BookingModel
from models.chat_room import AddChatRoomModel
from models.availability import AvailabilityModel
import utils.response as res
from dependencies import verify_token, verify_customer, verify_mate, verify_admin
from datetime import datetime, date
router = APIRouter(
    prefix="/controller",
    tags=["controller"],
    dependencies=[Depends(verify_token)]
)

@router.post("/add-booking", dependencies=[Depends(verify_customer)])
def add_booking(body: MateModel):
    from app import controller
    customer: UserAccount = controller.search_customer_by_id(Body.user_id)
    if customer == None:
        controller.add_log(False, "?", "Add Booking", "No Item", "?", "Customer not found")
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Customer not found")
    mate: UserAccount = controller.search_mate_by_id(body.mate_id)  
    if mate == None:
        controller.add_log(False, customer, "Add Booking", "No Item", "?", "Mate not found")
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    try:
        booking, transaction = controller.add_booking(customer, mate, body.date)
    except:
        controller.add_log(False, customer, "Add Booking", "No Item", mate, "Booking Incompleted (Try Deposit Money)")
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
    controller.add_log(True, customer, "Add Booking", "Booking", mate, "Booking Completed")
    return res.success_response_status(status.HTTP_200_OK, "Booked Successfully", data={"booking": booking.get_booking_details(), "transaction": transaction.get_transaction_details()})

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

@router.get("/get-customers")
def get_mates():
    from app import controller
    customer_list = controller.get_customers()
    if isinstance(customer_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Mate Success", data=[{'account_detail' : acc.get_account_details()} for acc in customer_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in add mate")

@router.get("/get-mate-by-username/{username}")
def get_mate_by_username(username: str):
    from app import controller
    mate_list = controller.get_mate_by_username(username)
    if isinstance(mate_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Mate Success", data=[{'account_detail' : acc.get_account_details()} for acc in mate_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "mate not found")

@router.get("/get-mate-by-gender/{gender}")
def get_mate_by_gender(gender: str):
    from app import controller
    if gender not in ["male", "female"]:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "gender not found")
    mate_list = controller.get_mate_by_gender(gender)
    if isinstance(mate_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Mate Success", data=[{'account_detail' : acc.get_account_details()} for acc in mate_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "mate not found")

@router.get("/get-mate-by-avalibility")
def get_mate_by_avalibility():
    from app import controller
    mate_list = controller.get_mate_by_avalibility()
    if isinstance(mate_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Mate Success", data=[{'account_detail' : acc.get_account_details()} for acc in mate_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "mate not found")

@router.post("/search-mate-by-condition")
def get_mate_by_condition(body: SearchMateModel):
    from app import controller
    print(body.name, body.location, body.gender_list, body.age, body.availability)
    mate_list = controller.search_mate_by_condition(body.name, body.location, body.gender_list, body.age, body.availability)
    if isinstance(mate_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Mate Success", data=[{'account_detail' : acc.get_account_details()} for acc in mate_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "mate not found")

@router.post("/add-post", dependencies=[Depends(verify_mate)])
def add_post(body: PostModel):
    from app import controller
    mate: Mate = controller.search_mate_by_id(Body.user_id)
    post: Post = controller.add_post(mate, body.description, body.picture)
    if post == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in add post")
    return res.success_response_status(status.HTTP_200_OK, "Add Post Success", data=post.get_post_details())

@router.get("/get-post")
def get_post():
    from app import controller
    post_list: list[Post] = controller.get_post()
    data_list = []
    for post in post_list:
        data_list.append(post.get_post_details())
    if post == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in read post")
    return res.success_response_status(status.HTTP_200_OK, "Get Post Success", data = data_list)

@router.get("/get-booking-by-admin", dependencies=[Depends(verify_admin)])
def get_booking():
    from app import controller
    booking_list: list = controller.get_all_booking()
    if isinstance(booking_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Booking Success", data=[booking.get_booking_details() for booking in booking_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in get booking")

@router.get("/get-booking", dependencies=[Depends(verify_customer)])
def get_booking():
    from app import controller
    customer: UserAccount = controller.search_customer_by_id(Body.user_id)
    booking_list: list = controller.get_booking(customer)
    if isinstance(booking_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Booking Success", data=[booking.get_booking_details() for booking in booking_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in get booking")

@router.get("/get-booking-by-id/{booking_id}")
def get_booking_by_id(booking_id: str):
    from app import controller
    result: Booking = controller.search_booking_by_id(booking_id)
    if result:
        return res.success_response_status(status.HTTP_200_OK, "Booking found", data=result.get_booking_details())
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Booking not found")

@router.get("/get-self-profile")
def get_self_profile():
    from app import controller
    account: UserAccount = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "UserAccount not found")
    return res.success_response_status(status.HTTP_200_OK, "Get Profile Success", data=account.get_account_details())

@router.get("/get-user-profile/{user_id}")
def get_user_profile(user_id: str):
    from app import controller
    account: Account = controller.search_account_by_id(user_id)
    if account == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "UserAccount not found")
    return res.success_response_status(status.HTTP_200_OK, "Get Profile Success", data=account.get_account_details())

@router.delete("/delete-booking/{booking_id}", dependencies=[Depends(verify_customer)])
def delete_booking(booking_id: str):
    from app import controller
    booking: Booking = controller.search_booking_by_id(booking_id)
    account: UserAccount = controller.search_account_by_id(Body.user_id)
    if booking == None or account == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Booking or UserAccount not found")
    deleted_booking: Union[Tuple[Booking, Transaction], Booking, None] = controller.delete_booking(booking, account)
    if isinstance(deleted_booking, tuple):
        return res.success_response_status(status.HTTP_200_OK, "Delete Booking Success", data={"booking": deleted_booking[0].get_booking_details(), "transaction": deleted_booking[1].get_transaction_details()})
    elif isinstance(deleted_booking, Booking):
        return res.success_response_status(status.HTTP_200_OK, "Delete Booking Success", data=deleted_booking.get_booking_details())
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in delete booking")

@router.post("/add-chat-room", dependencies=[Depends(verify_customer)])
def add_chat_room(body: AddChatRoomModel):
    from app import controller
    account_1: UserAccount = controller.search_account_by_id(Body.user_id)
    account_2: UserAccount = controller.search_account_by_id(body.receiver_id)
    chat_room: ChatRoomManeger = controller.add_chat_room(account_1, account_2)
    if chat_room == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "UserAccount not found")
    return res.success_response_status(status.HTTP_200_OK, "Add Chat Room Success", data=chat_room.get_chat_room_details())

@router.put("/edit-display-name")
def edit_display_name(body: EditDisplayNameModel):
    from app import controller
    account: UserAccount = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Edit displayname Error")
    edited_account: UserAccount = controller.edit_display_name(account, body.display_name)
    return res.success_response_status(status.HTTP_200_OK, "Edit displayname Success",  data=edited_account.get_account_details())
    
@router.put("/edit-pic-url")
def edit_pic_url(body: EditPicUrlModel):
    from app import controller
    account: UserAccount = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Send pic url Error")
    edited_account: UserAccount = controller.edit_pic_url(account, body.url)
    return res.success_response_status(status.HTTP_200_OK, "Edit pic url Success",  data=edited_account.get_account_details())
    
@router.put("/edit-money")
def edit_money(body: EditMoneyModel):
    from app import controller
    account: UserAccount = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Edit money Error")
    edited_account: UserAccount = controller.edit_money(account, body.amount)
    return res.success_response_status(status.HTTP_200_OK, "Edit money Success",  data=edited_account.get_account_details())

@router.get("/get-leaderboard")
def get_leaderboard():
    rank = 1
    from app import controller
    from internal.mate import Mate
    mate_list : list[Mate] = controller.get_leaderboard()
    my_list = []
    for mate in mate_list:
        if (mate.get_average_review_star() >= 0):
            my_list.append(mate)
    send_data = [{'account_detail' : acc.get_account_details()} for acc in my_list]
    for data in send_data:
        data["account_detail"]["rank"] = rank
        rank += 1
    if len(my_list):
        return res.success_response_status(status.HTTP_200_OK, "Get Leaderboard Success", data=send_data)
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "UserAccount not found")

@router.post("/add-amount", dependencies=[Depends(verify_customer)])
def add_amount(body: EditMoneyModel):
    from app import controller
    account: Account = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Edit money Error")
    account.amount = account.amount + body.amount
    transaction: Transaction = account.add_transaction(Transaction(account, account, body.amount))
    return res.success_response_status(status.HTTP_200_OK, "Edit money Success",  data=transaction.get_transaction_details())

@router.post("/del-amount", dependencies=[Depends(verify_mate)])
def del_amount(body: EditMoneyModel):
    from app import controller
    account: Account = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Edit money Error")
    account.amount = account.amount - body.amount
    transaction: Transaction = account.add_transaction(Transaction(account, account, body.amount))
    return res.success_response_status(status.HTTP_200_OK, "Edit money Success",  data=transaction.get_transaction_details())

@router.get("/get-log")
def get_log():
    from app import controller
    log_list = controller.get_log()
    if isinstance(log_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Log Success", data=controller.get_log())
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in get log")

@router.get("/get-transaction")
def get_transaction():
    from app import controller
    account: Account = controller.search_account_by_id(Body.user_id)
    transaction_list = account.transaction_list
    if isinstance(transaction_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Transaction Success", data=[transaction.get_transaction_details() for transaction in transaction_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in get transaction")

@router.get("/get-transaction-by-admin", dependencies=[Depends(verify_admin)])
def get_transaction_by_admin():
    from app import controller
    transaction_list = controller.get_all_transaction()
    if isinstance(transaction_list, list):
        return res.success_response_status(status.HTTP_200_OK, "Get Transaction Success", data=[transaction.get_transaction_details() for transaction in transaction_list])
    return res.error_response_status(status.HTTP_404_NOT_FOUND, "Error in get transaction")

@router.put("/edit-age")
def edit_age(body: EditAgeModel):
    from app import controller
    account: Account = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Edit Age Error")
    edited_account: Account = controller.edit_age(account, body.age)
    return res.success_response_status(status.HTTP_200_OK, "Edit Age Success",  data=edited_account.get_account_details())

@router.put("/edit-location")
def edit_location(body: EditLocationModel):
    from app import controller
    account: Account = controller.search_account_by_id(Body.user_id)
    if account == None:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Edit Location Error")
    edited_account: Account = controller.edit_location(account, body.location)
    return res.success_response_status(status.HTTP_200_OK, "Edit Location Success",  data=edited_account.get_account_details()) 

@router.get("/logs")
def get_log():
    from app import controller
    log_list = controller.log_list
    if len(log_list) == 0:
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Get Log Error")
    return res.success_response_status(status.HTTP_200_OK, "Get Log Success", data=[log.get_log_details() for log in log_list])
