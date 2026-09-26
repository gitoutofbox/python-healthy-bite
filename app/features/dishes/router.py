from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.auth import verifyToken
from app.core.dependencies import getDb
from app.features.dishes import schemas
from app.features.dishes import schemas, service

router = APIRouter(prefix="/dishes", tags=["Dishes"])

@router.post("/", response_model=schemas.DishResponse)
def createDish(dish: schemas.DishCreate, db: Session = Depends(getDb)):
    return service.createDish(dish, db)

@router.get("/")
def getDishes(pn: int = 1, ps: int = 1, search:str = Query(default=""), db: Session = Depends(getDb), user = Depends(verifyToken)):
    return service.getDishes(pn, ps, search, db)

@router.get("/{id}", response_model=schemas.DishResponse)
def getDish(id: int, db: Session = Depends(getDb)):
    return service.getDish(id, db)


@router.put("/{id}", response_model=schemas.DishResponse)
def updateDish(id: int, dish: schemas.DishCreate, db: Session = Depends(getDb)):
    return service.updateDish(id, dish, db)

@router.delete("/{id}")
def deleteDish(id:int, db: Session = Depends(getDb)):
    return service.deleteDish(id, db)