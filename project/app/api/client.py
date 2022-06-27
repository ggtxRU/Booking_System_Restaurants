
from math import ceil
from fastapi import APIRouter, Response
from typing import List

from app.api import crud
from app.models.tortoise import Restaurants, Tables

from app.models.pydantic import VisitTime
from tortoise.queryset import Q
from pprint import pprint

router = APIRouter()


@router.get("/available_restaurants/", tags=["Работа с клиентом"], 
description="Показать список подходящих ресторанов")
async def available_restaurants(visit_time: VisitTime, number_of_people: int):

    if number_of_people <= 8:
        tables = await Tables.filter(
            available_time__icontains=f'{visit_time}',
            total_number_of_seats__gte=number_of_people, 
            available_number_of_tables__gt=0).all().values()
            

        return tables
    else:
        restaurants = await Restaurants.all().count()
        
        tables = [await Tables.filter(available_time__icontains=f'{visit_time}', restaurants_id=i).all().values() for i in range(1,restaurants+1)]

        available_tables_restaurants = {f'{j["name"]}': (j['restaurants_id']) for i in tables for j in i if number_of_people / j['total_number_of_seats'] <= j['available_number_of_tables']}

        if len(available_tables_restaurants) != 0:
            return available_tables_restaurants

        else:
            available_count = {}
            for i in tables:
                for j in i:
                    available_count[j['restaurants_id']] = j['total_number_of_seats'] * j['available_number_of_tables']
            return available_count



        # restaurants_dict = {}
        # for i in tables:
        #     for j in i:


        #         if number_of_people / j['total_number_of_seats'] <= j['available_number_of_tables']:
        #             print("id=", j["id"], "rest id=", j["restaurants_id"], "in cicle")
        #             number_of_table_for_client = ceil(number_of_people / j['total_number_of_seats'])
        #             # return Response(f"Сдвинуть {number_of_table_for_client} {j['total_number_of_seats']}-местных столов в ресторане {j['restaurants_id']}")
        #             restaurants_dict[f"{j['name']}_rest_id_{j['restaurants_id']}"] = (number_of_table_for_client, j['restaurants_id'])

        # return restaurants_dict