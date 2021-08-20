from typing import List

from fastapi import FastAPI, Depends
from . import crud, models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/announce/', response_model=List[schemas.Announce])
def list_announce(db: Session = Depends(get_db)):
    return crud.get_announce(db=db)


@app.post('/announce/', response_model=schemas.Announce)
def create_announce(announce: schemas.AnnounceCreate, db: Session = Depends(get_db)):
    return crud.create_announce(db=db, announce=announce)


@app.put('/announce/{id}/', response_model=schemas.Announce)
def update_announce(announce: schemas.AnnounceUpdate, id: int = id, db: Session = Depends(get_db)):
    return crud.update_announce(db=db, announce=announce, id=id)


@app.delete('/announce/{id}/')
def update_announce(id: int = id, db: Session = Depends(get_db)):
    crud.delete_announce(db=db, id=id)
    return {}