import sqlalchemy as sa
from sqlalchemy.orm import relationship
from .base import Base
from .actor import Actor
from .location import Location
from .timeline_element import TimelineElement


class ReportedEvent(Base):
    __tablename__ = "reported_events2"

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
    updated_at = sa.Column(sa.DateTime, default=sa.func.now(),
                           onupdate=sa.func.now())
    what = sa.Column(sa.String)
    actor_id = sa.Column(sa.Integer, sa.ForeignKey('actors.id'))
    actor = relationship("Actor", back_populates="reported_events")
    timeline_element_id = sa.Column(sa.Integer,
                                    sa.ForeignKey('timeline_elements.id'))
    timeline_element = relationship("TimelineElement",
                                    back_populates="reported_events")
    location_id = sa.Column(sa.Integer, sa.ForeignKey('locations.id'))
    location = relationship("Location", back_populates="reported_events")
