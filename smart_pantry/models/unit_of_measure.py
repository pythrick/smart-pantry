from smart_pantry.models import AbstractBaseModel
from tortoise import fields


class UnitOfMeasure(AbstractBaseModel):
    name = fields.CharField(50, unique=True)
    abbrev = fields.CharField(5, unique=True)

    class Meta:
        table = "units_of_measure"
