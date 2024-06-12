from fastapi import FastAPI
from .database import engine, Base
from .routes import config
# from .exceptions import http_exception_handler
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(config.router)

from .exceptions import add_exception_handlers

add_exception_handlers(app)
