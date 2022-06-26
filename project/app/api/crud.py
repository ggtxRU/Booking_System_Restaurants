from typing import Any, List

from app.models.tortoise import Tables, Restaurants
from app.models.pydantic import RestaurantsPayloadSchema, TablesPayloadSchema
from app.models.pydantic import VisitTime


async def get_restaurants() -> List:
    order = await Restaurants.all().values()
    return order

async def get_tables(restaurants_id: int) -> List:
    order = await Tables.filter(restaurants_id=restaurants_id).values()
    return order


async def post_restaurant(RestaurantPayload: RestaurantsPayloadSchema) -> str:
    restaurant = Restaurants(name=RestaurantPayload.name, average_waiting_time=RestaurantPayload.average_waiting_time, average_price_check=RestaurantPayload.average_price_check)
    await restaurant.save()
    return restaurant.id


async def post_table(TablePayload: TablesPayloadSchema) -> str:
    restaurants_id = {"Karavella": 1, "Molodost": 2, "MeatAndSalat": 3}
    table = Tables(name=TablePayload.name, total_number_of_seats=TablePayload.total_number_of_seats, available_number_of_tables=6, restaurants_id=restaurants_id[TablePayload.restaurant])
    await table.save()
    return table.id

