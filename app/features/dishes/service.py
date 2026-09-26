from fastapi import APIRouter, FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.dependencies import getDb
# from database import engine, SessionLocal
import app.features.dishes.models as models, app.features.dishes.schemas as schemas
from app.core.auth import createToken, verifyToken

# models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/products", tags=["Products"])

# @router.post("/dish", response_model=schemas.DishResponse)
def createDish(dish: schemas.DishCreate, db: Session = Depends(getDb)):
    newDish = models.Dish(
        title=dish.title,
        desc=dish.desc,
    )
    db.add(newDish)
    db.commit()
    db.refresh(newDish)
    return newDish

# Get all dishes
# @router.get("/dishes")
def getDishes(pn: int = 1, ps: int = 1, search:str = Query(default=""), db: Session = Depends(getDb), user = Depends(verifyToken)):
    query = db.query(models.Dish)
    
    if(search):
        query = query.filter(models.Dish.title.ilike(f"%{search}%"))
  
    total = query.count()
    start = (pn-1) * ps
    dishes = query.offset(start).limit(ps).all()
    return{
        "pn":pn,
        "ps":ps,
        "total": total,
        "data": dishes
    }

# @router.get("/dishes/{id}", response_model=schemas.DishResponse)
def getDish(id: int, db: Session = Depends(getDb)):
    dish = db.query(models.Dish).filter(models.Dish.id == id).first()
    if not dish:
        raise HTTPException(status_code=404, detail= "Dish not found")
    return dish


# @router.put("/dishes/{id}", response_model=schemas.DishResponse)
def updateDish(id: int, dish: schemas.DishCreate, db: Session = Depends(getDb)):
    existingDish = db.query(models.Dish).filter(models.Dish.id == id).first()
    if not existingDish:
        raise HTTPException(status_code=404, detail="Dish not found")
    existingDish.title = dish.title
    existingDish.desc = dish.desc
    db.commit()
    db.refresh(existingDish)
    return existingDish


# @router.delete("/dishes/{id}")
def deleteDish(id:int, db: Session = Depends(getDb)):
    existingDish = db.query(models.Dish).filter(models.Dish.id == id).first()
    if not existingDish:
        raise HTTPException(status_code=404, detail="Dish not found")
    db.delete(existingDish)
    db.commit()
    return {"message": "Dish deleted successfully"}