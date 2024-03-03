from pydantic import BaseModel

class AddReviewMateModel(BaseModel):
    customer_id: str

class MateModel(BaseModel):
    mate_id: str