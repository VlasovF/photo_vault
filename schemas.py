from pydantic import BaseModel


class SchemaPhoto(BaseModel):
	id: int
	body: str
	format: str
	photo_set_id: int


class SchemaPhotoSet(BaseModel):
	id: int
