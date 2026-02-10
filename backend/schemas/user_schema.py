from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class userData(BaseModel):
    username: str
    age: int
    email: str
    address: str
    hashed_password: str
    creation_time: Optional[datetime] = None