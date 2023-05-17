-- create the database hbtn_0d_usa and table cities
-- create database
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
-- use database 
USE hbtn_0d_usa;
-- create table cities
CREATE TABLES IF NOT EXIT cities (id INT UNIQUE AUTO_INCREMENT NOT NULL, 
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
