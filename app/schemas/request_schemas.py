from pydantic import BaseModel
from datetime import datetime

class RequestLogSchema(BaseModel):
    id: int
    operation: str
    parameters: str
    result: str
    timestamp: datetime

    class Config:
        orm_mode = True  # allows compatibility with SQLAlchemy models