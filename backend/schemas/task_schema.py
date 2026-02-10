from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class taskData(BaseModel):
    title: str
    description: str
    assigned_user_id: int
    status: str
    due_date: datetime

class taskUpdateData(BaseModel):
    title: Optional[str]
    description: str
    assigned_user_id: int
    status: Optional[str]
    due_date: datetime
    completion_date: Optional[str]