import uuid

import pytest
from smart_pantry.schemas import ProductSchema


@pytest.fixture
def product_schema_from_orm(product):
    return ProductSchema.from_orm(product)


def test_product_schema_from_orm(product_schema_from_orm):
    assert isinstance(product_schema_from_orm.id, uuid.UUID)
