-- creates the database hbtn_0d_usa and the table cities
-- creates a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates a table cities
-- id INT unique, auto-generated, not null, primary key
-- states_id INT, not null, foreign key that references id 'states' table
-- name varchar not null
-- if table already exist it doesn't fail
CREATE TABLE IF NOT EXISTS cities
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	states_id INT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id),
	FOREIGN KEY(states_id)
		REFERENCES hbtn_0d_usa.states(id)
);
