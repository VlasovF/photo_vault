from typing import Union

from fastapi import APIRouter


from . import models, schemas
from databse import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)



router = APIRouter()


async def get_db():
	db =  SessionLocal()
	try:
		yield db
	finally:
		db.close()


@router.get("/")
async def root():
        return {'message': 'Hello World!'}


@router.get("/new_photo_set")
async def new_photo_set():
	db = await get_db()
	new_photo_set = models.PhotoSet()
	db.add(new_photo_set)
	db.commit()
	return {"photo_set_id": new_photo_set.id}


@router.post("/new_photo")
async def add_photo(photo_set_id: int, photo: schemas.SchemaPhoto):
	db = await get_db()
	photo_set = db.query(models.PhotoSet).filter(models.PhotoSet.id == photo_set_id).first()
	new_photo = models.Photo(body=photo.body, format=photo.format)
	photo_set.photo.add(new_photo)
	db.commit()
	return {"photo_set_id": photo_set.id, "photo_id": new_photo.id}
