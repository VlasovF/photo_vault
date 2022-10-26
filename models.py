from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base



class PhotoSet(Base):
        __table__ = "photo_set"
        id = Column(Integer, primary_key=True)
        photo = relationship("Photo")

        def __repr__(self):
                return "Photo Set %r" % self.id


class Photo(Base):
	__tablename__ = "photos"
	id = Column(Integer, primary_key=True)
	body = Column(String, nullable=False)
	format = Column(String(6), nullable=False)
	photo_set_id = relationship("PhotoSet")

	def __repr__(self):
		return "Photo %r" % self.id

