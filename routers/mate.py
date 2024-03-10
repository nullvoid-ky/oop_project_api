from fastapi import APIRouter, Depends, status, Body
import datetime
from models.review import *
from internal.account import Account
from internal.availability import Availability
from models.post import PostModel
from models.availability import AvailabilityModel
import utils.response as res
from dependencies import verify_token, verify_mate

router = APIRouter(
    prefix="/mate",
    tags=["mate"],
    dependencies=[Depends(verify_token)]
)

@router.post("/add-post", dependencies=[Depends(verify_mate)])
def add_post(body: PostModel):
    from app import controller
    mate = controller.search_mate_by_id(Body.user_id)
    if mate == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    mate.add_post(body.description, body.picture, body.timestamp)
    return res.success_response_status(status.HTTP_201_CREATED, "Post created")

@router.post("/add-availability", dependencies=[Depends(verify_mate)])
def add_availability(body: AvailabilityModel):
    from app import controller
    mate = controller.search_mate_by_id(Body.user_id)
    if mate == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    if mate.search_availability(body.date.year, body.date.month, body.date.day):
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Availability already exists")
    mate.add_availability(Availability(datetime.date(body.date.year, body.date.month, body.date.day), body.detail))
    return res.success_response_status(status.HTTP_201_CREATED, "Availability added")

@router.get("/get-availability/{mate_id}")
def get_availability(mate_id: str):
    from app import controller
    mate = controller.search_mate_by_id(mate_id)
    if mate == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    availability_list: list = mate.availability_list
    if len(availability_list) == 0:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "No availability")
    return res.success_response_status(status.HTTP_200_OK, "Get availability success", data=[availability.get_availability_details() for availability in availability_list])

@router.post("/add-review")
def add_review(body: ReviewCreation):
    from app import controller
    mate = controller.search_mate_by_id(body.mate_id)
    if mate == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    customer = controller.search_customer_by_id(Body.user_id)
    if customer == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Customer not found")
    review = mate.add_review_mate(customer, body.message, int(body.star))
    if review:
        return res.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=review.get_review_details())
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.get("/get-reviews/{mate_id}")
async def get_review(mate_id: str):
    from app import controller
    mate = controller.search_mate_by_id(mate_id)
    if mate == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    result = mate.get_review_mate()
    data_list = []
    for review in result:
        data_list.append(review.get_review_details())
    if len(data_list):
        return res.success_response_status(status.HTTP_200_OK, "Read Review Successfully", data=data_list)
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.delete("/del-review")
async def delete_review(body: ReviewDeletion):
    from app import controller
    mate = controller.search_mate_by_id(body.mate_id)
    result = mate.del_review_mate(body.review_id)
    if result:
        return res.success_response_status(status.HTTP_200_OK, "Delete Review Successfully", data=result.get_review_details())
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.get("/get-avarage-review-star/{mate_id}")
def get_average_review_star(mate_id):
    from app import controller
    mate = controller.search_mate_by_id(mate_id)
    if mate == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Mate not found")
    return res.success_response_status(status.HTTP_200_OK, "Get Avarage Review Star Successfully", data=mate.get_average_review_star())

@router.get("/get-mate-profile/{user_id}")
def get_user_profile(user_id: str):
    from app import controller
    from internal.mate import Mate
    account: Mate = controller.search_mate_by_id(user_id)
    if account == None:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "Account not found")
    return res.success_response_status(status.HTTP_200_OK, "Get Profile Success", data=account.get_account_details())
