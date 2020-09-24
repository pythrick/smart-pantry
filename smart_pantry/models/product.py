from smart_pantry.models import AbstractBaseModel
from tortoise import fields


class Product(AbstractBaseModel):
    name = fields.CharField(150, unique=True)

    class Meta:
        table = "products"
