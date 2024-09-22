from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class Notification(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(BaseModel):
    email: str
    password: str


class UserLoginResponse(BaseModel):
    success: bool
    message: str