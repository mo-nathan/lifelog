import sqlalchemy as sa
from sqlalchemy.orm import relationship
from .base import Base


class TimelineElement(Base):
    __tablename__ = "timeline_elements"

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
    updated_at = sa.Column(sa.DateTime,
                           default=sa.func.now(),
                           onupdate=sa.func.now())
    earliest = sa.Column(sa.DateTime, default=sa.func.now())
    latest = sa.Column(sa.DateTime, default=sa.func.now())
    estimated_start = sa.Column(sa.DateTime, default=sa.func.now())
    estimated_end = sa.Column(sa.DateTime, default=sa.func.now())
    reported_events = relationship("ReportedEvent",
                                   back_populates="timeline_element")
