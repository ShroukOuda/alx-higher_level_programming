-- createdatabase and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT PRIMARY KEY,	
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFENCES states(id), 
	name VARCHAR(256) NOT NULL);

