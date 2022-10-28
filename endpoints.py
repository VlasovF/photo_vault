from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Photo, PhotoSet, Base
from schemas import SchemaPhoto, SchemaPhotoSet
from database import SessionLocal, engine


Base.metadata.create_all(bind=engine)



router = APIRouter()


def get_db():
	db =  SessionLocal()
	try:
		yield db
	finally:
		db.close()


@router.get("/")
def root():
        return {'message': 'Hello World!'}


@router.get("/new_photo_set")
def new_photo_set(db: Session = Depends(get_db)):
	new_photo_set = PhotoSet()
	db.add(new_photo_set)
	db.commit()
	return {"photo_set_id": new_photo_set.id}


@router.post("/new_photo")
def add_photo(photo_set_id: int, photo: SchemaPhoto, db: Session = Depends(get_db)):
	photo_set = db.query(PhotoSet).filter(PhotoSet.id == photo_set_id).first()
	new_photo = Photo(body=photo.body, format=photo.format)
	photo_set.photo.add(new_photo)
	db.commit()
	return {"photo_set_id": photo_set.id, "photo_id": new_photo.id}
