-- =======================================
--  Script to initialize DB
--  Database: stock_db
-- =======================================

-- Create user and database
CREATE DATABASE stock_db;
CREATE USER stock_user WITH PASSWORD 'stock_pass';
GRANT ALL PRIVILEGES ON DATABASE stock_db TO stock_user;

-- Conect to db
\c stock_db;

-- ======================
-- Tables
-- ======================

-- Items table
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    sku VARCHAR(50) NOT NULL UNIQUE,
    ean13 VARCHAR(13) NOT NULL UNIQUE,
    stock INT NOT NULL DEFAULT 0
);

-- Movements table
CREATE TABLE stock_movements (
    id SERIAL PRIMARY KEY,
    item_id INT NOT NULL REFERENCES items(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    movement_type VARCHAR(10) NOT NULL CHECK (movement_type IN ('IN', 'OUT')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ======================
-- INSERTS
-- ======================

INSERT INTO items (sku, ean13, stock) VALUES
('SKU-001', '1234567890123', 50),
('SKU-002', '2345678901234', 20),
('SKU-003', '3456789012345', 100);


INSERT INTO stock_movements (item_id, quantity, movement_type) VALUES
(1, 50, 'IN'),
(2, 20, 'IN'),
(3, 100, 'IN');