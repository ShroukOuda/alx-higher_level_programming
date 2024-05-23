-- createdatabase and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT PRIMARY KEY, 
	constraint state_id INT FOREIGHN KEY REFERENCES states(id), 
	name VARCHAR(256) NOT NULL);

