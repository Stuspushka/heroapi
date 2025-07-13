from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from src import schemas, crud
from .database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/hero/", response_model=schemas.Hero)
def create_hero(name: str = Query(...), db: Session = Depends(get_db)):
    return crud.create_hero(db, name)

@app.get("/hero/", response_model=list[schemas.Hero])
def read_heroes(
    name: str = None,
    intelligence: int = None,
    intelligence__gte: int = None,
    intelligence__lte: int = None,
    strength: int = None,
    strength__gte: int = None,
    strength__lte: int = None,
    speed: int = None,
    speed__gte: int = None,
    speed__lte: int = None,
    power: int = None,
    power__gte: int = None,
    power__lte: int = None,
    db: Session = Depends(get_db),
):
    filters = {k: v for k, v in locals().items() if v is not None and k != "db"}
    return crud.get_heroes(db, filters)
