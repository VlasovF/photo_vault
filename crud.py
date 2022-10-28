from sqlalchemy.orm import Session

import models, schemas


def new_photo_set(db: Session):
	new_photo_set = models.PhotoSet()
	db.add(new_photo_set)
	db.commit()
	return	new_photo_set


def new_photo(photo_set_id: int, photo: schemas.SchemaPhoto, db: Session):
	photo_set = db.query(models.PhotoSet).filter(models.PhotoSet.id == photo_set_id).first()
	new_photo = models.Photo(body=photo.body, format=photo.format)
	photo_set.photo.add(new_photo)
	db.commit()
	return new_photo
