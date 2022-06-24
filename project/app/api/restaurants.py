from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import RestaurantsPayloadSchema

router = APIRouter()


@router.post("/restaurants/")
async def create_restaurant(payload: RestaurantsPayloadSchema):
    restaurant_id = await crud.post_restaurant(payload)
    response_object = {"id": restaurant_id, "name": payload.name}
    return response_object
