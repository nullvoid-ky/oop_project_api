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

@router.post("/add_review")
async def add_review(body: ReviewCreation):
    from main import controller
    mate = controller.search_mate_by_id(body.mate_id)
    result : dict = mate.add_review_mate(body.customer_id, body.message, body.star)
    if result:
        return res.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=result.get_review_detail())
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.get("/reviews")
async def see_review(body : MateReview):
    from main import controller
    mate = controller.search_mate_by_id(body.mate_id)
    result : dict = mate.get_review_mate()
    data_list = []
    for review in result:
        data_list.append(review.get_review_detail())
    if len(data_list):
        return res.success_response_status(status.HTTP_200_OK, "Read Review Successfully", data=data_list)
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.delete("/del_review")
async def delete_review(body: ReviewDeletion):
    from main import controller
    mate = controller.search_mate_by_id(body.mate_id)
    result : dict = mate.del_review_mate(body.review_id)
    if result:
        return res.success_response_status(status.HTTP_200_OK, "Delete Review Successfully", data=result.get_review_detail())
    return res.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
