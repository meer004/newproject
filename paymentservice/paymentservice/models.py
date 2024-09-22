from sqlmodel import SQLMODEL,Field
from typing import Optional

class Payment(SQLMODEL, table= True):
    id : Optional[int] = Field(default=None, primary_key=True)
    amount = float
    email = str
    status = bool
    