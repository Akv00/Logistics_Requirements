from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class ConfigurationNotFoundError(HTTPException):
    """
    Exception raised when a configuration for a specific country code is not found.
    Inherits from HTTPException and sets a 404 status code with a custom detail message.
    """
    def __init__(self, country_code: str):
        # Create a message indicating the missing configuration
        detail = f"Configuration for country code {country_code} not found"
        # Initialize the parent HTTPException with status code 404 and the custom detail message
        super().__init__(status_code=404, detail=detail)


class ConfigurationAlreadyExists(HTTPException):
    """
    Exception raised when a configuration for a specific country code already exists.
    Inherits from HTTPException and sets a 400 status code with a custom detail message.
    """
    def __init__(self, country_code: str):
        # Create a detailed message indicating the existing configuration
        detail = f"Configuration for country code {country_code} already exists"
        # Initialize the parent HTTPException with status code 400 and the custom detail message
        super().__init__(status_code=404, detail=detail)


def add_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        # Create a JSON response with the status code and detail message from the HTTPException
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

