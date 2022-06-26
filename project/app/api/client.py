from fastapi import APIRouter
from typing import List

from app.api import crud
from app.models.tortoise import Tables

from app.models.pydantic import VisitTime
from tortoise.queryset import Q


router = APIRouter()


@router.get("/available_restaurants/", tags=["Работа с клиентом"], 
description="Показать список подходящих ресторанов")
async def available_restaurants(visit_time: VisitTime, number_of_people: int):

    tables = await crud.get_tables_by_time(time=visit_time, number_of_people=number_of_people)
    return tables
    