from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database
from ..services.stock_service import StockService

router = APIRouter(prefix="/stock", tags=["Stock"])

def get_stock_service(db: Session = Depends(database.get_db)):
    return StockService(db)

@router.put("/{item_id}", response_model=schemas.ItemSchema)
def update_stock(item_id: int, stock_data: schemas.UpdateStockSchema, service: StockService = Depends(get_stock_service)):
    item = service.update_stock(item_id, stock_data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/{item_id}/movements", response_model=List[schemas.StockMovementSchema])
def stock_movements(item_id: int, service: StockService = Depends(get_stock_service)):
    return service.get_stock_movements(item_id)

@router.get("/items", response_model=List[schemas.ItemSchema])
def list_stock_items(db: Session = Depends(database.get_db)):
    service = StockService(db)
    return service.list_items()