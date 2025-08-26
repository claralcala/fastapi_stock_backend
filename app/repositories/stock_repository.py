from sqlalchemy.orm import Session
from .. import models

class StockRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_item(self, item_id: int):
        return self.db.query(models.Item).filter(models.Item.id == item_id).first()
    
    def get_all_items(self):
        return self.db.query(models.Item).all()

    def update_item_stock(self, item, quantity: int, movement_type: str):
        if movement_type == "IN":
            item.stock += quantity
        elif movement_type == "OUT":
            item.stock -= quantity
        self.db.commit()
        self.db.refresh(item)
        return item

    def create_movement(self, item_id: int, quantity: int, movement_type: str):
        movement = models.StockMovement(
            item_id=item_id,
            quantity=quantity,
            movement_type=movement_type
        )
        self.db.add(movement)
        self.db.commit()
        return movement

    def get_movements(self, item_id: int):
        return self.db.query(models.StockMovement).filter(models.StockMovement.item_id == item_id).all()