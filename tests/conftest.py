import asyncio
import os

import pytest
from faker import Faker
from fastapi.testclient import TestClient
from smart_pantry.app import app
from smart_pantry.models import Product, UnitOfMeasure
from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="module")
def client():
    yield TestClient(app)


@pytest.fixture(scope="function", autouse=True)
def initialize_tests(request):
    db_url = os.environ.get("TORTOISE_TEST_DB", "sqlite://:memory:")
    initializer(["smart_pantry.models"], db_url=db_url, app_label="models")
    request.addfinalizer(finalizer)


@pytest.yield_fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def fake():
    return Faker("pt_BR")


@pytest.fixture()
@pytest.mark.asyncio
async def unit_of_measure(fake) -> UnitOfMeasure:
    return await UnitOfMeasure.create(name=fake.word(), abbrev=fake.pystr(max_chars=3))


@pytest.fixture()
@pytest.mark.asyncio
async def product(fake, unit_of_measure) -> Product:
    return await Product.create(name=fake.word(), unit_of_measure=unit_of_measure)
