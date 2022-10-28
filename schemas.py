from pydantic import BaseModel


class SchemaPhoto(BaseModel):
	body: str
	format: str
	photo_set_id: int

