import uuid

import pytest
from fastapi.testclient import TestClient
from smart_pantry.schemas import UnitOfMeasureSchema


@pytest.fixture
def create_request(client: TestClient, fake):
    response = client.post(
        "/api/v1/units-of-measure",
        json={
            "name": fake.pystr(min_chars=5, max_chars=20),
            "abbrev": fake.pystr(min_chars=1, max_chars=3),
        },
    )

    return response.json()


def test_units_of_measure_resource_create_uuid(create_request):
    assert str(uuid.UUID(create_request["id"], version=4)) == create_request["id"]


def test_units_of_measure_resource_create_schema(create_request):
    assert UnitOfMeasureSchema(**create_request)
