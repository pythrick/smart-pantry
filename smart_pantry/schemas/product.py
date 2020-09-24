import uuid

from pydantic import BaseModel


class UnitOfMeasureSchema(BaseModel):
    name: str
    abbrev: str

    class Config:
        orm_mode = True


class ProductSchema(BaseModel):
    id: uuid.UUID
    name: str
    unit_of_measure: UnitOfMeasureSchema = None

    class Config:
        orm_mode = True


class ProductInSchema(BaseModel):
    name: str
    unit_of_measure: str
