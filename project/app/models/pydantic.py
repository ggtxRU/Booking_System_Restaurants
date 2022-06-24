from pydantic import BaseModel

from enum import Enum as Enum_


class Enum(Enum_):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


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
