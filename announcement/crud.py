from sqlalchemy.orm import Session
from . import models, schemas


def get_announce(db: Session):
    return db.query(models.Announcement).all()


def create_announce(db: Session, announce: schemas.AnnounceCreate):
    db_announce = models.Announcement(**announce.dict())
    db.add(db_announce)
    db.commit()
    db.refresh(db_announce)
    return db_announce


def update_announce(db: Session, announce: schemas.AnnounceUpdate, id: int):
    db_announce = db.query(models.Announcement).get(id)

    db_announce.title = announce.title
    db_announce.category = announce.category
    db_announce.date = announce.date
    db_announce.description = announce.description
    db_announce.connect = announce.connect

    db.commit()
    db.refresh(db_announce)
    return db_announce


def delete_announce(db: Session, id: int):
    db_announce = db.query(models.Announcement).get(id)
    db.delete(db_announce)
    db.commit()


def favorite_announce(db: Session, id: int, favorite: bool=True):
    db_announce = db.query(models.Announcement).get(id)
    db_announce.favorite = favorite

    db.commit()
    db.refresh(db_announce)
    return db_announce
