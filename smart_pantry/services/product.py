from typing import List

from fastapi import HTTPException
from smart_pantry.models import Product, UnitOfMeasure
from smart_pantry.schemas import ProductInSchema, ProductSchema
from starlette import status
from tortoise.exceptions import DoesNotExist


async def create(product: ProductInSchema) -> ProductSchema:
    data = product.dict()
    try:
        unit_of_measure = await UnitOfMeasure.get(abbrev=data.pop("unit_of_measure"))
    except DoesNotExist as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Invalid unit of measurement"
        ) from e
    product = await Product.create(**data, unit_of_measure=unit_of_measure)
    return ProductSchema.from_orm(product)


async def list() -> List[ProductSchema]:
    return [
        ProductSchema.from_orm(product)
        for product in await Product.all().select_related("unit_of_measure")
    ]
