from fastapi import APIRouter
from typing import List

from app.api import crud

from app.models.pydantic import TablesPayloadSchema
from app.models.tortoise import TablesSchema


router = APIRouter()

@router.get("/tables/all",
            tags=["Столы"],
            description="Получить данные по всем столам в базе данных.",
            )
async def get_all(restaurants_id:int) -> List[TablesSchema]:
    response_object = await crud.get_tables(restaurants_id=restaurants_id)
    return response_object


@router.post("/tables/create_new/")
async def create_table(payload: TablesPayloadSchema):
    print(payload)
    table_id = await crud.post_table(payload)
    response_object = {"id":table_id, "name":payload.name}
    return response_object


