from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class LivestreamCreate(BaseModel):
    title: str
    description: Optional[str] = None
    product_ids: List[int]
    scheduled_time: datetime
    created_by: int


class LivestreamOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    product_ids: List[int]
    scheduled_time: datetime
    created_by: int
    status: str

    class Config:
        orm_mode = True
