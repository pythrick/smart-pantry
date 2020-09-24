from smart_pantry.models import AbstractBaseModel
from tortoise import fields


class Product(AbstractBaseModel):
    name = fields.CharField(150, unique=True)
    unit_of_measure = fields.ForeignKeyField(
        "models.UnitOfMeasure", "products", fields.RESTRICT, null=False, required=True
    )

    class Meta:
        table = "products"
