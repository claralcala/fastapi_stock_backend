from pydantic import BaseModel
from datetime import datetime
from typing import List

class UpdateStockSchema(BaseModel):
    quantity: int
    movement_type: str  # 'IN' o 'OUT'

class StockMovementSchema(BaseModel):
    id: int
    item_id: int
    quantity: int
    movement_type: str
    created_at: datetime

    class Config:
        orm_mode = True

class ItemSchema(BaseModel):
    id: int
    sku: str
    ean13: str
    stock: int

    class Config:
        orm_mode = True