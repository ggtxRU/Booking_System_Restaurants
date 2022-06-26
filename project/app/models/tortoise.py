from typing import List
from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator




class Restaurants(models.Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(max_length=29)
    average_waiting_time=fields.IntField()
    average_price_check=fields.IntField()

    tables: fields.ReverseRelation["Tables"]

    def __str__(self):
        return self.name

class Tables(models.Model):
    id=fields.IntField(pk=True)
    name=fields.TextField(null=False)
    total_number_of_seats=fields.IntField(null=False)
    available_number_of_tables = fields.IntField(null=False)
    time09_11 = fields.BooleanField(default=True)
    time11_13 = fields.BooleanField(default=True)
    time13_15 = fields.BooleanField(default=True)
    time15_17 = fields.BooleanField(default=True)
    time17_19 = fields.BooleanField(default=True)
    time19_21 = fields.BooleanField(default=True)
    time21_23 = fields.BooleanField(default=True)

    restaurants: fields.ForeignKeyRelation[Restaurants] = fields.ForeignKeyField("models.Restaurants", related_name="tables")

    def __str__(self):
        return self.name


ResturantsSchema = pydantic_model_creator(Restaurants)
TablesSchema = pydantic_model_creator(Tables, exclude="restaurants")

