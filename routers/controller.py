from fastapi import APIRouter,status
from ..models.controller import reviewMateModel
from ..utils.response import Responses 
from main import controller
import uvicorn

router = APIRouter(
    prefix="/controller",
    tags=["controller"],
)

@router.post("/add_review")
async def add_review(body: reviewMateModel):
    review = controller.add_review_mate(body.customer_id, body.mate_id, body.message, body.star)
    if isinstance(review, None):
        return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
    return Responses.success_response_status(status.HTTP_200_OK, "Added Review Successfully", review)
