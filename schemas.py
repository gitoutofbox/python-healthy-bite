from pydantic import BaseModel
from datetime import datetime

#Input schema
class DishCreate(BaseModel):
    title: str
    desc: str

class DishResponse(BaseModel):
    id: int
    title: str
    desc: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attribute = True  