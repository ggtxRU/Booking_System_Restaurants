from typing import List
from pydantic import BaseModel
from enum import Enum as Enum_


class Enum(Enum_):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

class VisitTime(str, Enum):
    time09_11="09:00-11:00"
    time11_13="11:00-13:00"
    time13_15="13:00-15:00"
    time15_17="15:00-17:00"
    time17_19="17:00-19:00"
    time19_21="19:00-21:00"
    time21_23="21:00-23:00"



class RestaurantsName(str, Enum):
    Karavella="Karavella"
    Molodost="Molodost"
    MeatAndSalat="MeatAndSalat"


class RestaurantsPayloadSchema(BaseModel):
    name: str
    average_waiting_time: int
    average_price_check: int


class TablesPayloadSchema(BaseModel):
    name: str
    total_number_of_seats: int
    restaurant: str
