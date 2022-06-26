
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
        tables = (await Tables.filter(
            available_time__icontains=f'{visit_time}',
            total_number_of_seats__gte=number_of_people, 
            available_number_of_tables__gt=0).all().values()
            )

        return tables
    else:
        restaurants = (await Restaurants.all().count())
        
        tables = [await Tables.filter(available_time__icontains=f'{visit_time}', restaurants_id=i).all().values() for i in range(1,restaurants+1)]



        # for table in range(len(tables)):
        #     if tables[table]["total_number_of_seats"] + tables[table + 1]["total_number_of_seats"] >= number_of_people:
        #         rest1, rest2 = tables[table]["restaurants_id"], tables[table +1]["restaurants_id"]

        #         variants.append({"restaurants_id": (rest1, rest2) })

          

        restaurants_dict = {}
        for i in tables:
            # i

            # [{'id': 1, 'name': '4-seats table', 'total_number_of_seats': 4, 'available_number_of_tables': 6, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 1}, {'id': 2, 'name': '3-seats table', 'total_number_of_seats': 3, 'available_number_of_tables': 2, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 1}, {'id': 3, 'name': '2-seats table', 'total_number_of_seats': 2, 'available_number_of_tables': 2, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 1}]

            # {'id': 4, 'name': '3-seats table', 'total_number_of_seats': 3, 'available_number_of_tables': 3, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 2}]

            # [{'id': 5, 'name': '8-seats table', 'total_number_of_seats': 8, 'available_number_of_tables': 2, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 3}, {'id': 6, 'name': '3-seats table', 'total_number_of_seats': 3, 'available_number_of_tables': 4, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 3}]
            for j in i:
                print(j["id"], j["restaurants_id"])
                print(number_of_people / j['total_number_of_seats'])

                if number_of_people / j['total_number_of_seats'] <= j['available_number_of_tables']:
                    print("id=", j["id"], "rest id=", j["restaurants_id"], "in cicle")
                    number_of_table_for_client = ceil(number_of_people / j['total_number_of_seats'])
                    # return Response(f"Сдвинуть {number_of_table_for_client} {j['total_number_of_seats']}-местных столов в ресторане {j['restaurants_id']}")
                    restaurants_dict[f"{j['name']}_rest_id_{j['restaurants_id']}"] = (number_of_table_for_client, j['restaurants_id'])

                # j

                # {'id': 1, 'name': '4-seats table', 'total_number_of_seats': 4, 'available_number_of_tables': 6, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 1}
                # {'id': 2, 'name': '3-seats table', 'total_number_of_seats': 3, 'available_number_of_tables': 2, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 1}
                # {'id': 3, 'name': '2-seats table', 'total_number_of_seats': 2, 'available_number_of_tables': 2, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 1}


                # {'id': 4, 'name': '3-seats table', 'total_number_of_seats': 3, 'available_number_of_tables': 3, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 2}


                # {'id': 5, 'name': '8-seats table', 'total_number_of_seats': 8, 'available_number_of_tables': 2, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 3}
                # {'id': 6, 'name': '3-seats table', 'total_number_of_seats': 3, 'available_number_of_tables': 4, 'available_time': '09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00', 'busy_time': None, 'restaurants_id': 3}

                # for k in j:
                #     print(f"{j[k]}")
                #     print()
                # print()
                # print()
                    

        return restaurants_dict