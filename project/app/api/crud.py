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

async def get_tables_by_time(time: str, number_of_people: int):
    timing = {"09:00-11:00": "time09_11",
              "11:00-13:00": "time11_13",
              "13:00-15:00": "time13_15",
              "15:00-17:00": "time15_17",
              "17:00-19:00": "time17_19",
              "19:00-21:00": "time19_21",
              "21:00-23:00": "time21_23",
            }

    if timing[f"{time[0:]}"] == "time09_11":
        tables = await Tables.filter(time17_19=True, total_number_of_seats__gte=number_of_people).all().values()
    if timing[f"{time[0:]}"] == "time11_13":
        tables = await Tables.filter(time17_19=True, total_number_of_seats__gte=number_of_people).all().values()
    if timing[f"{time[0:]}"] == "time13_15":
        tables = await Tables.filter(time17_19=True, total_number_of_seats__gte=number_of_people).all().values()   
    if timing[f"{time[0:]}"] == "time15_17":
        tables = await Tables.filter(time17_19=True, total_number_of_seats__gte=number_of_people).all().values()
    if timing[f"{time[0:]}"] == "time17_19":
        tables = await Tables.filter(time17_19=True, total_number_of_seats__gte=number_of_people).all().values()
    if timing[f"{time[0:]}"] == "time19_21":
        tables = await Tables.filter(time17_19=True, total_number_of_seats__gte=number_of_people).all().values()
    if timing[f"{time[0:]}"] == "time21_23":
        tables = await Tables.filter(time17_19=True, total_number_of_seats__gte=number_of_people).all().values()
    return tables