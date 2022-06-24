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
    time10_12=fields.BooleanField(default=True)
    time12_14 = fields.BooleanField(default=True)
    time14_16 = fields.BooleanField(default=True)
    time18_20 = fields.BooleanField(default=True)
    time22_00 = fields.BooleanField(default=True)

    restaurants: fields.ForeignKeyRelation[Restaurants] = fields.ForeignKeyField("models.Restaurants", related_name="tables")

    def __str__(self):
        return self.name
