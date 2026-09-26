from sqlalchemy import Column, Integer, String, Text, DateTime
from app.db.session import Base
from datetime import datetime

class Dish(Base):
    __tablename__ = "hb_dish"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    desc = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
