from pydantic import BaseModel, PositiveFloat, EmailStr, validators
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase): # Única classe que se comunica com o ORM
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel): # O update não precisa ser para todos os campos, então todos são opcionais
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None