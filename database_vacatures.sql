CREATE DATABASE vacaturesite

CREATE USER  'Alexander'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON  * . * TO 'Alexander'@'localhost';

CREATE TABLE vacatures (
		id_vacature INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
		date_added DATE,
		job_description TEXT,
		job_title VARCHAR(100),
		
	);
CREATE TABLE reports (
		id_contact INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
		naam MEDIUMTEXT NOT NULL,
		telefoonnummer VARCHAR(11) NOT NULL,
		email_adres VARCHAR(100) NOT NULL,
		onderwerp VARCHAR(50) NOT NULL,
		bericht TEXT NOT NULL,
	
	);