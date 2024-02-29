from fastapi import APIRouter,status
from ..models.review import reviewMateModel
from ..internal.response import Responses 
import uvicorn

router = APIRouter(
    prefix="/review",
    tags=["review"],
)

@router.post("/add_review")
async def add_review(body: reviewMateModel):
    from main import controller
    result : dict = controller.add_review_mate(body.customer_id, body.mate_id, body.message, body.star)
    if result:
        return Responses.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=result)
    return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
