from pydantic import BaseModel

class PaymentModel(BaseModel):
    booking_id: str