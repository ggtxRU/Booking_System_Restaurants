
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
    available_number_of_tables=fields.IntField(null=False)
    available_time=fields.TextField(default="09:00-11:00, 11:00-13:00, 13:00-15:00, 15:00-17:00, 17:00-19:00, 19:00-21:00, 21:00-23:00")
    busy_time=fields.TextField(null=True)

    restaurants: fields.ForeignKeyRelation[Restaurants] = fields.ForeignKeyField("models.Restaurants", related_name="tables")

    def __str__(self):
        return self.name


ResturantsSchema = pydantic_model_creator(Restaurants)
TablesSchema = pydantic_model_creator(Tables, exclude="restaurants")

