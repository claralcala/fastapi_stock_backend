from sqlalchemy.orm import Session
from ..schemas import UpdateStockSchema
from ..repositories.stock_repository import StockRepository

class StockService:
    def __init__(self, db: Session):
        self.repo = StockRepository(db)

    def list_items(self):
        return self.repo.get_all_items()

    def update_stock(self, item_id: int, stock_data: UpdateStockSchema):
        item = self.repo.get_item(item_id)
        if not item:
            return None
        item = self.repo.update_item_stock(item, stock_data.quantity, stock_data.movement_type)
        self.repo.create_movement(item_id, stock_data.quantity, stock_data.movement_type)
        return item

    def get_stock_movements(self, item_id: int):
        return self.repo.get_movements(item_id)