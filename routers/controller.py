from fastapi import APIRouter, status, Depends, Body

from models.controller import ReviewModel
from internal.response import Responses
from dependencies import verify_token 

router = APIRouter(
    prefix="/controller",
    tags=["controller"],
    dependencies=[Depends(verify_token)]
)

@router.post("/add_review")
def add_review(body: ReviewModel):
    from app import controller
    review = controller.add_review_mate(Body.user_id, body.mate_id, body.message, body.star)
    if isinstance(review, None):
        return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
    return Responses.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=review)