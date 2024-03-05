from fastapi import APIRouter,status
from ..models.review import ReviewModel
from ..internal.response import Responses 
import uvicorn

router = APIRouter(
    prefix="/review",
    tags=["review"],
)

@router.post("/add_review")
async def add_review(body: ReviewModel):
    from main import controller
    result : dict = controller.add_review_mate(body.customer_id, body.mate_id, body.message, body.star)
    if result:
        return Responses.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=result.get_review_detail())
    return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.get("/reviews")
async def see_review(body: ReviewModel):
    from main import controller
    result : dict = controller.add_review_mate(body.customer_id, body.mate_id, body.message, body.star)
    if result:
        return Responses.success_response_status(status.HTTP_200_OK, "Read Review Successfully", data=result.get_review_detail())
    return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

@router.delete("/del_review")
async def delete_review(body: ReviewModel):
    from main import controller
    result : dict = controller.add_review_mate(body.customer_id, body.mate_id, body.message, body.star)
    if result:
        return Responses.success_response_status(status.HTTP_200_OK, "Delete Review Successfully", data=result.get_review_detail())
    return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
