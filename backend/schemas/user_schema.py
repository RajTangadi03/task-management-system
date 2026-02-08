from datetime import datetime
from pydantic import BaseModel

class userData(BaseModel):
    username: str
    age: int
    email: str
    address: str
    hashed_password: str
    creation_time: datetime