import asyncio

from fastapi import FastAPI
from loguru import logger
from .db import init_db
from .api import welcome, restaurants, tables, client, fillingdb




def create_application() -> FastAPI:

    application = FastAPI()
    application.include_router(welcome.router)
    application.include_router(restaurants.router)
    application.include_router(tables.router)
    application.include_router(fillingdb.router)
    application.include_router(client.router)
    return application

app = create_application()


@app.on_event("startup")
async def startup_event() -> None:
    init_db(app)
