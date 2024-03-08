# from fastapi import APIRouter,status
# from ..models.review import *
# from ..internal.response import Responses 
# import uvicorn

# router = APIRouter(
#     prefix="/review",
#     tags=["review"],
# )

# @router.post("/add_review")
# async def add_review(body: ReviewCreation):
#     from app import controller
#     result : dict = controller.add_review_mate(body.customer_id, body.mate_id, body.message, body.star)
#     if result:
#         return Responses.success_response_status(status.HTTP_200_OK, "Added Review Successfully", data=result.get_review_detail())
#     return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

# @router.get("/reviews")
# async def see_review(body : ReviewRead):
#     from app import controller
#     result : dict = controller.search_review(body.mate_id)
#     data_list = []
#     for review in result:
#         data_list.append(review.get_review_detail())
#     if len(data_list):
#         return Responses.success_response_status(status.HTTP_200_OK, "Read Review Successfully", data=data_list)
#     return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")

# @router.delete("/del_review")
# async def delete_review(body: ReviewDeletion):
#     from app import controller
#     result : dict = controller.del_review_mate(body.mate_id, body.review_id)
#     if result:
#         return Responses.success_response_status(status.HTTP_200_OK, "Delete Review Successfully", data=result.get_review_detail())
#     return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, "Incomplete")
