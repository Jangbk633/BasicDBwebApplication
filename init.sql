CREATE DATABASE IF NOT EXISTS ticket_db
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_general_ci;

USE ticket_db;

CREATE TABLE IF NOT EXISTS ticket (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    date DATE NOT NULL,
    description TEXT,
    category VARCHAR(100) NOT NULL DEFAULT 'etc'
)CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

INSERT INTO ticket (title, price, date, description, category)
VALUES 
    ('Concert 1', 50000, '2024-12-25', 'Concert Discription 1', "concert"),
    ('Sports 1', 30000, '2024-12-30', 'Sports Discription 1', "sports"),
    ('Musical 1', 70000, '2024-12-28', 'Musical Discription 1', "musical"),
    ('Concert 2', 65000, '2025-1-12', 'Concert Discription 2', "concert"),
    ('Sports 2', 16000, '2025-1-22', 'Sports Discription 2', "sports"),
    ('Musical 2', 67000, '2025-1-03', 'Musical Discription 2', "musical"),
    ('Concert 3', 34000, '2024-12-27', 'Concert Discription 3', "concert"),
    ('Sports 3', 26000, '2025-1-30', 'Sports Discription 3', "sports"),
    ('Musical 3', 96000, '2024-12-24', 'Musical Discription 3', "musical"),
    ('Concert 4', 42000, '2025-1-08', 'Concert Discription 4', "concert"),
    ('Sports 4', 15000, '2025-2-1', 'Sports Discription 4', "sports"),
    ('Musical 4', 75000, '2024-12-21', 'Musical Discription 4', "musical");