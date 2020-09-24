import uuid
from typing import Dict, List

import pytest
from fastapi.testclient import TestClient
from smart_pantry.models import Product, UnitOfMeasure
from smart_pantry.schemas import ProductSchema


@pytest.fixture
def create_request(unit_of_measure: UnitOfMeasure, client: TestClient, fake):
    response = client.post(
        "/api/v1/products",
        json={
            "name": fake.pystr(min_chars=5, max_chars=20),
            "unit_of_measure": unit_of_measure.abbrev,
        },
    )

    return response.json()


def test_products_resource_create_uuid(create_request):
    assert str(uuid.UUID(create_request["id"], version=4)) == create_request["id"]


def test_products_resource_create_schema(create_request):
    assert ProductSchema(**create_request)


@pytest.fixture
def list_request(product: Product, client: TestClient, fake):
    return client.get("/api/v1/products").json()


def test_products_resource_list(list_request: List[Dict[str, str]]):
    assert isinstance(list_request, list)


def test_products_resource_list_len(list_request: List[Dict[str, str]]):
    assert len(list_request) == 1


def test_products_resource_list_schema(list_request):
    assert ProductSchema(**list_request[0])
