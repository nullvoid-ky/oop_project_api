from pydantic import BaseModel

class reviewMateModel(BaseModel):
    customer_id : str
    mate_id : str
    message : str
    star : int