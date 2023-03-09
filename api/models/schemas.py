from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


# Definição dos modelos de entrada/saída para a API
class TaxiFareBase(BaseModel):
    pickup_datetime: datetime
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    passenger_count: int
    fare_amount: float

class TaxiFareCreate(TaxiFareBase):
    pass

class TaxiFareUpdate(TaxiFareBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class TaxiFare(TaxiFareBase):
    id: int

    class Config:
        orm_mode = True


class TaxiFareList(BaseModel):
    __root__: List[TaxiFare]


# Definição dos modelos de entrada/saída para o script de batch

class TaxiFareBatch(BaseModel):
    pickup_datetime: str
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    passenger_count: int
    fare_amount: float


class TaxiFareBatchList(BaseModel):
    TaxiFares: List[TaxiFareBatch]
