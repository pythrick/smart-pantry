import uuid
from typing import List

import pytest
from smart_pantry.schemas import ProductInSchema, ProductSchema
from smart_pantry.services import product as product_service


@pytest.fixture
def product_in_schema(fake):
    return ProductInSchema(name=fake.pystr(min_chars=3, max_chars=15),)


@pytest.fixture
async def product_schema(product_in_schema):
    return await product_service.create(product_in_schema)


def test_product_service_create_type(product_schema: ProductSchema):
    assert isinstance(product_schema, ProductSchema)


def test_product_service_create_id(product_schema: ProductSchema):
    assert isinstance(product_schema.id, uuid.UUID)


@pytest.fixture
async def products_schema(product_schema: ProductSchema) -> List[ProductSchema]:
    return await product_service.list()


@pytest.mark.asyncio
def test_product_service_list(products_schema: List[ProductSchema]):
    assert isinstance(products_schema[0], ProductSchema)
