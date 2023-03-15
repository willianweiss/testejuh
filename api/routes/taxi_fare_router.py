from typing import List

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session
from api.auth.auth_bearer import JWTBearer
from api.database.connection import get_db
from api.models.schemas import TaxiFareCreate, TaxiFareUpdate, TaxiFare
from api.models.taxi_fare_model import TaxiFareModel
import pandas as pd

router = APIRouter(
    tags=["taxi_fares"],
    dependencies=[Depends(JWTBearer())],
    responses={404: {"description": "Not found"}},
)


@router.post("/taxi_fares", response_model=TaxiFare)
async def create_taxi_fare(
    taxi_fare: TaxiFareCreate,
    db: Session = Depends(get_db),
):
    new_taxi_fare = TaxiFareModel(**taxi_fare.dict())
    db.add(new_taxi_fare)
    db.commit()
    db.refresh(new_taxi_fare)
    return new_taxi_fare


@router.get("/taxi_fares/{taxi_fare_id}", response_model=TaxiFare)
async def read_taxi_fare(
    taxi_fare_id: int,
    db: Session = Depends(get_db),
):
    if (
        taxi_fare := db.query(TaxiFareModel)
        .filter(TaxiFareModel.id == taxi_fare_id)
        .first()
    ):
        return taxi_fare
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Taxi fare not found")


@router.put("/taxi_fares/{taxi_fare_id}", response_model=TaxiFare)
async def update_taxi_fare(
    taxi_fare_id: int,
    taxi_fare: TaxiFareUpdate,
    db: Session = Depends(get_db),
):
    existing_taxi_fare = db.query(TaxiFareModel).filter(TaxiFareModel.id == taxi_fare_id).first()
    if not existing_taxi_fare:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Taxi fare not found")
    for var, value in vars(taxi_fare).items():
        setattr(existing_taxi_fare, var, value) if value else None
    db.commit()
    db.refresh(existing_taxi_fare)
    return existing_taxi_fare


@router.delete("/taxi_fares/{taxi_fare_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_taxi_fare(
    taxi_fare_id: int,
    db: Session = Depends(get_db),
):
    existing_taxi_fare = db.query(TaxiFareModel).filter(TaxiFareModel.id == taxi_fare_id).first()
    if not existing_taxi_fare:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Taxi fare not found")
    db.delete(existing_taxi_fare)
    db.commit()
    return None


@router.get("/taxi_fares", response_model=List[TaxiFare])
async def read_all_taxi_fares(
    db: Session = Depends(get_db),
):
    return db.query(TaxiFareModel).all()
