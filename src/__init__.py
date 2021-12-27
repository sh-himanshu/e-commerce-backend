__version__ = "0.1.0"

from fastapi import FastAPI

from . import loader


# ASGI Server
app = FastAPI(
    title="e-commerce-backend",
    description="eCommerce Python REST API\
    \n ### Features:\
    \n - Fast",
    openapi_url="/api/openapi.json",
    docs_url=None,
    redoc_url="/redoc",
)

# Load endpoints from "/routes"
loader.load_routes()
