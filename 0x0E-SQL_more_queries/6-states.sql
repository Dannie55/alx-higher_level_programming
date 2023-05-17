-- create the database hbtn_0d_usa and the table states on MySQL server.
-- creates a database
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- create table state in hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, PRIMARY KEY(id));
