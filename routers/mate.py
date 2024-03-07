from fastapi import APIRouter, Depends, status, Body
import datetime
from models.review import *
from internal.account import Account
from internal.availability import Availablility
from models.post import PostModel
from models.availability import AvailabilityModel
import utils.response as res
from dependencies import verify_token, verify_mate

router = APIRouter(
    prefix="/mate",
    tags=["mate"],
    dependencies=[Depends(verify_token)]
)

@router.post("/create-post", dependencies=[Depends(verify_mate)])
def add_post(body: PostModel):
    from app import controller
    mate: Account = controller.search_mate_by_id(Body.user_id)
    mate.add_post(body.description, body.picture, body.timestamp)
    return res.success_response_status(status.HTTP_201_CREATED, "Post created")

@router.post("/add-available", dependencies=[Depends(verify_mate)])
def add_availablility(body: AvailabilityModel):
    from app import controller
    mate: Account = controller.search_mate_by_id(Body.user_id)
    if mate.search_availablility(body.date.year, body.date.month, body.date.day):
        return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Availablility already exists")
    mate.add_availablility(Availablility(datetime.date(body.date.year, body.date.month, body.date.day), body.detail))
    return res.success_response_status(status.HTTP_201_CREATED, "Availablility added")

@router.get("/get-availability/{mate_id}")
def get_availablility(mate_id: str):
    from app import controller
    mate: Account = controller.search_mate_by_id(mate_id)
    availablility_list: list = mate.availablility_list
    if len(availablility_list) == 0:
        return res.error_response_status(status.HTTP_404_NOT_FOUND, "No availablility")
    return res.success_response_status(status.HTTP_200_OK, "Get availablility success", data=[availablility.get_availablility_details() for availablility in availablility_list])

@router.post("/add-review")
async def add_review(body: ReviewCreation):
    from app import controller
    mate: Account = controller.search_mate_by_id(body.mate_id)
    review = mate.add_review_mate(body.customer_id, body.message, body.star)
    if review:
        return res.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=review.get_review_details())
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.get("/get-review/{mate_id}")
async def get_review(mate_id: str):
    from app import controller
    mate: Account = controller.search_mate_by_id(mate_id)
    review_list = []
    for review in mate.review_list:
        review_list.append(review.get_review_details())
    if len(review_list):
        return res.success_response_status(status.HTTP_200_OK, "Get Review Successfully", data=[r.get_review_details() for r in review_list])
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.delete("/del-review")
async def delete_review(body: ReviewDeletion):
    from app import controller
    mate: Account = controller.search_mate_by_id(body.review_id)
    review = mate.del_review_mate(body.review_id)
    if review:
        return res.success_response_status(status.HTTP_200_OK, "Delete Review Successfully", data=review.get_review_details())
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
