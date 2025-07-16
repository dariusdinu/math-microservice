from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.session import Base

class RequestLog(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    parameters = Column(String)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
