from pydantic import BaseModel

class ReviewCreation(BaseModel):
    mate_id : str
    message : str
    star : int

class ReviewDeletion(BaseModel):
    review_id : str
