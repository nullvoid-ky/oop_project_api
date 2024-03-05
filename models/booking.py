from pydantic import BaseModel

class BookingModel(BaseModel):
    booking_id: str