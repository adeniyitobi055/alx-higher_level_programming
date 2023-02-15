-- creates the database hbtn_0d_usa and table states on MySQL server
-- creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- creates the table states on my server
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
	name VARCHAR(256),
	PRIMARY KEY(id)
);
