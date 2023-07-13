-- script that creates a `users` table
-- if table does not exist
CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY (id)
);

