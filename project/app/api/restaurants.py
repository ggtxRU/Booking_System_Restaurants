from typing import List
from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import RestaurantsPayloadSchema
from app.models.tortoise import ResturantsSchema


router = APIRouter()


@router.post("/restaurants/")
async def create_restaurant(payload: RestaurantsPayloadSchema):
    restaurant_id = await crud.post_restaurant(payload)
    response_object = {"id": restaurant_id, "name": payload.name}
    return response_object


@router.get("/restaurants/all",
            tags=["Рестораны"],
            description="Получить данные по всем ресторанам в базе данных.",
            response_model=List[ResturantsSchema]
            )
async def get_all() -> List[ResturantsSchema]:
    response_object = await crud.get_restaurants()
    return response_object


