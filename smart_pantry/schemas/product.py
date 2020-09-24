import uuid

from pydantic import BaseModel


class ProductSchema(BaseModel):
    id: uuid.UUID
    name: str

    class Config:
        orm_mode = True


class ProductInSchema(BaseModel):
    name: str
