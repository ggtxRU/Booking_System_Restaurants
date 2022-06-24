import asyncio

from fastapi import FastAPI
from loguru import logger
from .db import init_db
from .api import welcome, restaurants, tables
from .logs.loguru_config import init_logging



def create_application() -> FastAPI:
    init_logging()
    logger.info("Initializing Application [START]")
    application = FastAPI()
    application.include_router(welcome.router)
    application.include_router(restaurants.router)
    application.include_router(tables.router)
    return application

app = create_application()


@app.on_event("startup")
async def startup_event() -> None:
    init_db(app)
