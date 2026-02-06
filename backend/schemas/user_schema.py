from datetime import datetime
from pydantic import BaseModel

class userData(BaseModel):
    name: str
    age: int
    email: str
    address: str
    password: str
    creation_time: datetime