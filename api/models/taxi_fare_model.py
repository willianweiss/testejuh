from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaxiFareModel(Base):
    __tablename__ = 'taxi_fare'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pickup_datetime = Column(DateTime, nullable=False)
    pickup_longitude = Column(Float, nullable=False)
    pickup_latitude = Column(Float, nullable=False)
    dropoff_longitude = Column(Float, nullable=False)
    dropoff_latitude = Column(Float, nullable=False)
    passenger_count = Column(Integer, nullable=False)
    fare_amount = Column(Float, nullable=False)
