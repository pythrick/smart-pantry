import os
from typing import List

import sentry_sdk
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from smart_pantry.schemas import (ProductInSchema, ProductSchema,
                                  UnitOfMeasureInSchema, UnitOfMeasureSchema)
from smart_pantry.services import product as product_service
from smart_pantry.services import unit_of_measure as unit_of_measure_service

app = FastAPI()


products: List[ProductSchema] = []


@app.post("/api/v1/units-of-measure")
async def register_unit_of_measure(
    unit_of_measure: UnitOfMeasureInSchema,
) -> UnitOfMeasureSchema:
    return await unit_of_measure_service.create(unit_of_measure)


@app.post("/api/v1/products")
async def register_product(product: ProductInSchema) -> ProductSchema:
    return await product_service.create(product)


@app.get("/api/v1/products")
async def list_products() -> List[ProductSchema]:
    return await product_service.list()


register_tortoise(
    app,
    db_url=os.getenv("DATABASE_URL", "sqlite://db.sqlite3"),
    modules={"models": ["smart_pantry.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


sentry_sdk.init(
    os.getenv("SENTRY_DSN"), traces_sample_rate=1.0, environment=os.getenv("SENTRY_ENV")
)
