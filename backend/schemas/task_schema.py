from datetime import datetime
from pydantic import BaseModel

class taskData(BaseModel):
    name: str
    age: int
    email: str
    address: str
    password: str
    creation_time: datetime