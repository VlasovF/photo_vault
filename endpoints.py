from typing import Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
import crud, schemas



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
	new_photo_set = crud.new_photo_set(db=db)
	return {"photo_set_id": new_photo_set.id}


@router.post("/new_photo")
def add_photo(photo_set_id: int, photo: schemas.SchemaPhoto, db: Session = Depends(get_db)):
	new_photo = crud.new_photo(photo_set_id=photo_set_id, photo=photo, db=db)
	return {"photo_set_id": new_photo.photo_set_id, "photo_id": new_photo.id}
