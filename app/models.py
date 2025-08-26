from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    ean13 = Column(String(13), unique=True, index=True, nullable=False)
    stock = Column(Integer, default=0)
    movements = relationship("StockMovement", back_populates="item")

class StockMovement(Base):
    __tablename__ = "stock_movements"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer)
    movement_type = Column(String)  # 'IN' o 'OUT'
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    item = relationship("Item", back_populates="movements")