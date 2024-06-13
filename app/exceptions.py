from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

class ConfigurationNotFoundError(HTTPException):
    def __init__(self, country_code: str):
        detail = f"Configuration for country code {country_code} not found"
        super().__init__(status_code=404, detail=detail)


class ConfigurationAlreadyExists(HTTPException):
    def __init__(self, country_code: str):
        detail = f"Configuration for country code {country_code} already exists"
        super().__init__(status_code=404, detail=detail)


def add_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

