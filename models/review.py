from pydantic import BaseModel

class ReviewModel(BaseModel):
    customer_id : str
    mate_id : str
    message : str
    star : int