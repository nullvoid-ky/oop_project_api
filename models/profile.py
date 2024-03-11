from pydantic import BaseModel

class EditDisplayNameModel(BaseModel):
    display_name: str

class EditPicUrlModel(BaseModel):
    url: str

class EditMoneyModel(BaseModel):
    amount: int

class EditAgeModel(BaseModel):
    age: int

class EditLocationModel(BaseModel):
    location: str

class EditPriceModel(BaseModel):
    price: int