from fastapi import FastAPI
from .database import engine, Base
from .routers import stock_router
from fastapi.middleware.cors import CORSMiddleware

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stock API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],        
)

app.include_router(stock_router.router)