from pydantic import BaseModel

class AddReviewMateModel(BaseModel):
    customer_id: str

class Date(BaseModel):
    year: int
    month: int
    day: int

class MateModel(BaseModel):
    mate_id: str
    date: Date