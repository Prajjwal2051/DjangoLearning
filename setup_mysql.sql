-- MySQL Setup Script for NIE College Trainer Management System
-- Run this script as MySQL root user:
-- sudo mysql < setup_mysql.sql
-- OR
-- mysql -u root -p < setup_mysql.sql

-- Create database
CREATE DATABASE IF NOT EXISTS nie_college_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user (change password as needed)
CREATE USER IF NOT EXISTS 'nie_user'@'localhost' IDENTIFIED BY 'nie_password_123';

-- Grant privileges
GRANT ALL PRIVILEGES ON nie_college_db.* TO 'nie_user'@'localhost';

-- Flush privileges
FLUSH PRIVILEGES;

-- Show databases to confirm
SHOW DATABASES;

SELECT 'Database setup completed successfully!' AS Status;
