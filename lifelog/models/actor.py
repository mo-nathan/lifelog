import sqlalchemy as sa
from sqlalchemy.orm import relationship
from .base import Base


class Actor(Base):
    __tablename__ = "actors"

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
    updated_at = sa.Column(sa.DateTime,
                           default=sa.func.now(),
                           onupdate=sa.func.now())
    full_name = sa.Column(sa.String)
    short_name = sa.Column(sa.String)
    email = sa.Column(sa.String)
    description = sa.Column(sa.String)
    reported_events = relationship("ReportedEvent",
                                   back_populates="actor")
