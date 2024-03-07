from pydantic import BaseModel

class ReviewCreation(BaseModel):
    customer_id : str
    mate_id : str
    message : str
    star : int

class ReviewDeletion(BaseModel):
    mate_id : str
    review_id : str

class ReviewRead(BaseModel):
    mate_id : str