from pydantic import BaseModel

class ReviewModel(BaseModel):
    mate_id : str
    message : str
    star : int