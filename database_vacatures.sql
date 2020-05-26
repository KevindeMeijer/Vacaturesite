CREATE DATABASE vacaturesite

CREATE USER  'Alexander'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON  * . * TO 'Alexander'@'localhost';

CREATE TABLE vacatures (
		id_vacature INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
		date_added DATE NOT NULL,
		job_description TEXT NOT NULL,
		job_title TEXT NOT NULL,
		
	);
CREATE TABLE reports (
		id_contact INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
		telefoonnummer INTEGER NOT NULL,
		email_adres VARCHAR(100) NOT NULL,
		onderwerp VARCHAR(50) NOT NULL,
		bericht TEXT NOT NULL,
	
	);