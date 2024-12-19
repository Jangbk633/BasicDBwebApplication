CREATE DATABASE IF NOT EXISTS ticket_db;

USE ticket_db;

CREATE TABLE IF NOT EXISTS ticket (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    date DATE NOT NULL,
    description TEXT
);

INSERT INTO ticket (title, price, date, description)
VALUES 
    ('Concert', 50000, '2024-12-25', 'Concert Discription'),
    ('Sports', 30000, '2024-12-30', 'Sports Discription'),
    ('Musical', 70000, '2024-12-20', 'Musical Discription');