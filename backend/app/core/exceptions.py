from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.logging import logger

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error"
        }
    )