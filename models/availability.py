from pydantic import BaseModel
from models.mate import Date

class AvailabilityModel(BaseModel):
    date: Date
    detail: str

class AddAvailabilityModel(BaseModel):
    day: int
    month: int
    year: int
    detail: str