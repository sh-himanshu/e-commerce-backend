__version__ = "0.1.0"

from fastapi import APIRouter, FastAPI

from . import loader
from .db import exit_db, init_db


# ASGI Server
app = FastAPI(
    title="e-commerce-backend",
    description="""
eCommerce Python REST API
### Features:
- Fast""",
    openapi_url="/api/openapi.json",
    docs_url=None,
    redoc_url="/redoc",
    on_startup=[init_db],
    on_shutdown=[exit_db],
)


V1 = APIRouter()


# Load all routes
loader.load_routes()


app.include_router(V1, prefix="/v1", tags=["v1"])
