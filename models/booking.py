from pydantic import BaseModel

class BookingModel(BaseModel):
    booking_id: str

class AddBookingModel(BaseModel):
    mate_id: str
    amount: int