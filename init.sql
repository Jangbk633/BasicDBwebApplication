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
    ('Concert', 50000, '2024-12-25', 'Concert Discription', "concert"),
    ('Sports', 30000, '2024-12-30', 'Sports Discription', "sports"),
    ('Musical', 70000, '2024-12-20', 'Musical Discription', "musical");