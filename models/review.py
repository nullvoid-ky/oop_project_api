from pydantic import BaseModel

class ReviewCreation(BaseModel):
    customer_id : str
    message : str
    mate_id : str
    star : int

class ReviewDeletion(BaseModel):
    review_id : str
    mate_id : str

class MateReview(BaseModel):
    mate_id : str