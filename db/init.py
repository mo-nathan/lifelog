from sqlalchemy import (
    create_engine,
    func,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    String,
)
 
engine = create_engine('sqlite:///lifelog.db', echo=True)
Base = declarative_base()

 
########################################################################
# class Actor(Base):
#     __tablename__ = "actors"

#     id = Column(Integer, primary_key = True)
#     name = Column(String)
#     unique_description = Column(String)


class ReportedEvent(Base):
    __tablename__ = "reported_events"
 
    id = Column(Integer, primary_key = True)

    # Who
    recorder = Column(String)

    # What
    what = Column(String)

    # When
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    earliest = Column(DateTime, default=func.now())
    latest = Column(DateTime, default=func.now())
    estimated_start = Column(DateTime, default=func.now())
    estimated_end = Column(DateTime, default=func.now())

    # Where
    location_description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    location_error_in_meters = Column(Float)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
print
new_event = ReportedEvent()
new_event.recorder = "Nathan Wilson"
new_event.what = "Started this database"

NATHANS_OFFICE = ("SE corner room, first floor, 68 Bay Rd., "
                  "North Falmouth, MA 02556")
new_event.location_description = NATHANS_OFFICE
new_event.latitude = 41.646702
new_event.longitude = -70.622723
new_event.location_error_in_meters = 5

session.add(new_event)

session.commit()
