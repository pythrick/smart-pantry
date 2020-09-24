from smart_pantry.models import UnitOfMeasure
from tortoise.contrib.pydantic import pydantic_model_creator

UnitOfMeasureSchema = pydantic_model_creator(UnitOfMeasure)
UnitOfMeasureInSchema = pydantic_model_creator(
    UnitOfMeasure, exclude_readonly=True, exclude=("id",)
)
