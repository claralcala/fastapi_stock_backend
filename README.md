# FastAPI Stock Manager

Pequeña aplicación de gestión de inventario con **FastAPI + PostgreSQL + SQLAlchemy**.


## Estructura del proyecto

fastapi_stock/
├─ app/
│  ├─ main.py
│  ├─ database.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ repositories/         # Acceso a DB
│  │  └─ stock_repository.py
│  ├─ services/             # Lógica de negocio
│  │  └─ stock_service.py
│  └─ routers/              # Endpoints
│     └─ stock_router.py
├─ alembic/                 # Migraciones de DB
├─ init_db.sql              # Script para crear tablas e insertar datos iniciales
├─ requirements.txt
└─ README.md

## Requisitos previos

- Python 3.9+
- PostgreSQL instalado 
- Node.js + npm 

## ⚙️ Instalación Backend

Clonar el repositorio:
    ```bash
   git clone 
   cd fastapi_stock


Crear y activar entorno virtual:

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


Instalar dependencias:

pip install -r requirements.txt


Configuración de PostgreSQL:

Crear la base de datos ejecutando el script init_db.sql:
psql -U postgres -f init_db.sql

Crea:
Base de datos stock_db
Usuario stock_user (password stock_pass)
Tablas items y stock_movements
Datos iniciales
Ejecutar el servidor FastAPI:

uvicorn app.main:app --reload

Acceso a la documentación en:

http://127.0.0.1:8000/docs

Endpoints principales

GET /stock/items → Lista todos los ítems con sku, ean13, stock
PUT /stock/items/{item_id} → Actualiza stock (IN/OUT)
GET /stock/movements → Lista historial de movimientos


Notas
Usuario de BD: stock_user
Contraseña: stock_pass
Base de datos: stock_db