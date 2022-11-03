import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings

from apis.base import api_router
from db.session import engine
from db.base import Base


def include_router(router_app):
    router_app.include_router(api_router)


def configure_static(static_app):
    static_app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    application = FastAPI(title=settings.PROJECT_NAME,
                          version=settings.PROJECT_VERSION)
    include_router(application)
    configure_static(application)
    create_tables()
    return application


app = start_application()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
