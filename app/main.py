import logging
from fastapi import FastAPI, Request, Response
from .database import SessionLocal, engine, Base
from .routes import config
# from .exceptions import http_exception_handler

# Configure logging for the application
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create all database tables based on the models defined in the Base metadata
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI application
app = FastAPI()

# Include the router from the config module to add the API endpoints to the app
app.include_router(config.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    # Default response in case of an internal server error
    response = Response("Internal server error", status_code=500)
    try:
        # Create a new database session and assign it to the request state
        request.state.db = SessionLocal()

        # Call the next middleware or request handler and get the response
        response = await call_next(request)
    finally:
        # Ensure the database session is closed after the request is processed
        request.state.db.close()

    # Return the generated response
    return response

from .exceptions import add_exception_handlers

# Add custom exception handlers to the FastAPI application
add_exception_handlers(app)
