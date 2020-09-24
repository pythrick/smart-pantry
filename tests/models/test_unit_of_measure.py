import uuid

import pytest
from smart_pantry.models import UnitOfMeasure


@pytest.mark.asyncio
async def test_unit_of_measure(unit_of_measure: UnitOfMeasure):
    assert isinstance(unit_of_measure.pk, uuid.UUID)


@pytest.mark.asyncio
async def test_unit_of_measure_str(unit_of_measure: UnitOfMeasure):
    assert str(unit_of_measure) == str(unit_of_measure.pk)


@pytest.mark.asyncio
async def test_unit_of_measure_repr(unit_of_measure: UnitOfMeasure):
    assert (
        repr(unit_of_measure)
        == f"{unit_of_measure.__class__.__name__}<{unit_of_measure}>"
    )
