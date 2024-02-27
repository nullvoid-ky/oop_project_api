import datetime
from fastapi import status
from internal.post import Post
from utils.response import Responses

from fastapi import FastAPI
import uvicorn

# Creating an app object
app = FastAPI()

class Mate:
    def __init__(self, post, picture):
        self.__post = post
        self.__picture = picture
        self.__post_list = []
        self.id

    @property
    def post(self):
        return self.__post

    @property
    def picture(self):
        return self.__picture

#Responses.error_response_status(status.HTTP_400_BAD_REQUEST, f"Type Error.")

    def create_post(self, description, picture):
        if not isinstance(description, str):
            return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, f"Expected description in str, but got {type(description)} instead.")
        if not isinstance(picture, str):
             return Responses.error_response_status(status.HTTP_400_BAD_REQUEST, f"Expected picture in str, but got {type(picture)} instead.")
        timestamp = datetime.datetime.now()
        Post(description, picture, timestamp)
        self.__post_list.append(Post)
        return Responses.success_response_status(200, "Post Success",
        {
            "description" : description,
            "picture" : picture,
            "timestamp" : timestamp
        })

        




        