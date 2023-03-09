from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TaxiFareModel(Base):
    __tablename__ = "taxi_fare"
    id = Column(Integer, primary_key=True, index=True)
    pickup_datetime = Column(DateTime)
    pickup_longitude = Column(Float)
    pickup_latitude = Column(Float)
    dropoff_longitude = Column(Float)
    dropoff_latitude = Column(Float)
    passenger_count = Column(Integer)
    fare_amount = Column(Float)
