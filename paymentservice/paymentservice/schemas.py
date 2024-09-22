from sqlmodel import SQLModel
from typing  import Optional

class PaymentBase(SQLModel):
    amount = float
    email = str
    status = bool
    

class PaymentCreate(PaymentBase):
    pass

class PaymentList(PaymentBase):
    id: int

class PaymentDetail(PaymentBase):
    id: int

class PaymentResponse(PaymentBase):
    id: int
    status: bool
    