from fastapi import APIRouter
from internal.mate import Mate 
from models.post import PostModel

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

mate = Mate()
@router.post("/create-post")
async def create_post(body: PostModel):
    return mate.create_post(body.description, body.picture, body.timestamp)
