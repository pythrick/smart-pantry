import uuid

import pytest
from smart_pantry.models import Product


@pytest.mark.asyncio
async def test_product(product: Product):
    assert isinstance(product.pk, uuid.UUID)


@pytest.mark.asyncio
async def test_product_str(product: Product):
    assert str(product) == str(product.pk)


@pytest.mark.asyncio
async def test_product_repr(product: Product):
    assert repr(product) == f"{product.__class__.__name__}<{product}>"
