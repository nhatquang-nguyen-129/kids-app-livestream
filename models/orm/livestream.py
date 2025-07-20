from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, JSON
from sqlalchemy.sql import func
from database.base import Base
import enum


class LivestreamStatus(str, enum.Enum):
    scheduled = "scheduled"
    live = "live"
    ended = "ended"
    canceled = "canceled"


class Livestream(Base):
    __tablename__ = "livestreams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    scheduled_time = Column(DateTime, nullable=False)
    product_ids = Column(JSON, nullable=False)  # list[int]
    created_by = Column(Integer, nullable=False)
    status = Column(Enum(LivestreamStatus), default=LivestreamStatus.scheduled)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
