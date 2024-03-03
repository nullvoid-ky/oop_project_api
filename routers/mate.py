from fastapi import APIRouter, Depends, status
from internal.mate import Mate 
from models.post import PostModel
from dependencies import verify_token
import utils.response as res

router = APIRouter(
    prefix="/post",
    tags=["post"],
    dependencies=[Depends(verify_token)]
)

mate = Mate()
@router.post("/create-post")
async def add_post(body: PostModel):
    mate.add_post(body.description, body.picture, body.timestamp)
    return res.success_response_status(status.HTTP_201_CREATED, "Post created")
    