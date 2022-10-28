from fastapi import FastAPI

from models import Base
from database import engine
from endpoints import router



Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:

    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()
