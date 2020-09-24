import uuid

import pytest
from smart_pantry.schemas import UnitOfMeasureSchema


@pytest.fixture
def unit_of_measure_schema_from_orm(unit_of_measure):
    return UnitOfMeasureSchema.from_orm(unit_of_measure)


def test_unit_of_measure_schema_from_orm(unit_of_measure_schema_from_orm):
    assert isinstance(unit_of_measure_schema_from_orm.id, uuid.UUID)
