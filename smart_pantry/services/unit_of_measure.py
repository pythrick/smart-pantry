from smart_pantry.models import UnitOfMeasure
from smart_pantry.schemas import UnitOfMeasureInSchema, UnitOfMeasureSchema


async def create(unit_of_measure: UnitOfMeasureInSchema) -> UnitOfMeasureSchema:
    data = unit_of_measure.dict()
    unit_of_measure = await UnitOfMeasure.create(**data)
    return await UnitOfMeasureSchema.from_tortoise_orm(unit_of_measure)
