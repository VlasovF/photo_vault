from sqlalchemy.orm import Session

import models, schemas


def new_photo_set(db: Session):
	new_photo_set = models.PhotoSet()
	db.add(new_photo_set)
	db.commit()
	return	new_photo_set


def new_photo(photo: schemas.SchemaPhoto, db: Session):
	new_photo = models.Photo(
			body=photo.body,
			format=photo.format,
			photo_set_id=photo.photo_set_id)
	db.add(new_photo)
	db.commit()
	return new_photo
