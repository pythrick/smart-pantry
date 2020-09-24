from typing import List

from smart_pantry.models import Product
from smart_pantry.schemas import ProductInSchema, ProductSchema


async def create(product: ProductInSchema) -> ProductSchema:
    product = await Product.create(**product.dict())
    return ProductSchema.from_orm(product)


async def list() -> List[ProductSchema]:
    return [ProductSchema.from_orm(product) for product in await Product.all()]
