from datetime import datetime
from pydantic import BaseModel

class taskData(BaseModel):
    title: str
    description: str
    assigned_user_id: int
    status: str
    due_date: datetime