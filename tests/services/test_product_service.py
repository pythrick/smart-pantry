import uuid
from typing import List

import pytest
from fastapi import HTTPException
from smart_pantry.models import UnitOfMeasure
from smart_pantry.schemas import ProductInSchema, ProductSchema
from smart_pantry.services import product as product_service


@pytest.fixture
def product_in_schema(fake, unit_of_measure: UnitOfMeasure):
    return ProductInSchema(
        name=fake.pystr(min_chars=3, max_chars=15),
        unit_of_measure=unit_of_measure.abbrev,
    )


@pytest.fixture
async def product_schema(product_in_schema):
    return await product_service.create(product_in_schema)


def test_product_service_create_type(product_schema: ProductSchema):
    assert isinstance(product_schema, ProductSchema)


def test_product_service_create_id(product_schema: ProductSchema):
    assert isinstance(product_schema.id, uuid.UUID)


@pytest.mark.asyncio
async def test_product_service_create_with_invalid_unit_of_measure(fake):
    product = ProductInSchema(
        name=fake.pystr(min_chars=5, max_chars=15),
        unit_of_measure=fake.pystr(min_chars=1, max_chars=3),
    )
    with pytest.raises(HTTPException):
        await product_service.create(product)


@pytest.fixture
async def products_schema(product_schema: ProductSchema) -> List[ProductSchema]:
    return await product_service.list()


@pytest.mark.asyncio
def test_product_service_list(products_schema: List[ProductSchema]):
    assert isinstance(products_schema[0], ProductSchema)
