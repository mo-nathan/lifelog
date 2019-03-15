import sqlalchemy as sa
from sqlalchemy.orm import relationship
from .base import Base


class Location(Base):
    __tablename__ = "locations"

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
    updated_at = sa.Column(sa.DateTime,
                           default=sa.func.now(),
                           onupdate=sa.func.now())
    description = sa.Column(sa.String)
    latitude = sa.Column(sa.Float)
    longitude = sa.Column(sa.Float)
    error_in_meters = sa.Column(sa.Float)
    reported_events = relationship("ReportedEvent",
                                   back_populates="location")
