import asyncio
from typing import List
from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import RestaurantsPayloadSchema
from app.models.tortoise import ResturantsSchema, Tables, Restaurants


router = APIRouter()


@router.post("/fillingdb/", 
            tags=["Заполнение базы данных данными, указанными в ТЗ."],
            description="<strong>База данных будет заполнена следующими данными:</strong>\n\n\n<i><u>«Каравелла»</u></i>\n\n10 столиков: 6 столиков вмещает до 4 человек. 2 столика вмещают до 3 человек. 2 столика вмещает до 2 человек;\n\nСреднее время ожидания блюда: 30 минут;\n\nСредний чек: 2000 рублей.\n\n\n\n<i><u>«Молодость»</u></i>\n\n\n3 столика, каждый из которых вмещает 3 человека;\nСреднее время ожидания блюда: 15 минут;\nСредний чек: 1000 рублей.\n\n\n\n<i><u>«Мясо и Салат»</u></i>\n\n\n6 столиков: 2 столика вмещает до 8 человек. 4 столика вмещают до 3 человек;\n\nСреднее время ожидания блюда: 60 минут;\n\nСредний чек: 1500 рублей. "
)
async def create_restaurants():
    """
    :available_restaurants: кортеж с данными ресторанов

    :available_restaurants_tables: кортеж, с данными о столиках ресторанов:

    --> example:
            :available_restaurants_tables[0]: - столики в ресторане
            :available_restaurants_tables[0][1]: - название столика
            :available_restaurants_tables[0][2]: - количество мест за столиком
            :available_restaurants_tables[0][0]: - количество данных столиков в ресторане
            
    id ресторанов:

    Karavella: 1
    Molodost: 2 
    MeatAndSalat: 3
    """

    available_restaurants = (
        ("Karavella", 30, 2000),
        ("Molodost", 15, 1000),
        ("MeatAndSalat", 60, 1500)
    )

    available_restaurants_tables = (
            (6, "4-seats table", 4, 1), 
            (2, "3-seats table", 3, 1), 
            (2, "2-seats table", 2, 1),

            (3, "3-seats table", 3, 2),

            (2,"8-seats table", 8, 3),
            (4, "3-seats table", 3, 3)
    )

    """Создаем сущности ресторанов в БД"""
    [await Restaurants(
        name=available_restaurants[i][0],
        average_waiting_time=available_restaurants[i][1],
        average_price_check=available_restaurants[i][2])
        .save()
        for i in range(0, len(available_restaurants))]

    await asyncio.sleep(0.3)
    """Создаем столики для ресторанов"""
    [await Tables(
        name=available_restaurants_tables[i][1],
        total_number_of_seats=available_restaurants_tables[i][2],
        available_number_of_tables=available_restaurants_tables[i][0],
        restaurants_id=available_restaurants_tables[i][3])
        .save() 
        for i in range(len(available_restaurants_tables))]





