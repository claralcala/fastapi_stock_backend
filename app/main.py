from fastapi import FastAPI
from .database import engine, Base
from .routers import stock_router

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stock API")

app.include_router(stock_router.router)