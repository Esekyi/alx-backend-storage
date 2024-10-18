-- SQL script that creates a table users
-- with a unique constraint on the column email
CREATE TABLE users (
	id SERIAL PRIMARY KEY NOT NULL,
	email VARCHAR(255) NOT NULL unique,
	name VARCHAR(255)
) IF NOT EXISTS;
