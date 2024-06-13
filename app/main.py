import logging
from fastapi import FastAPI, Request, Response
from .database import SessionLocal, engine, Base
from .routes import config
# from .exceptions import http_exception_handler

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(config.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

from .exceptions import add_exception_handlers

add_exception_handlers(app)
