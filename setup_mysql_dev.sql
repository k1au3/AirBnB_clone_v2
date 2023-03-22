-- script that prepares a mysql server for the project

-- Create a database hbnb_dev_db without the script failing.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a user of database and the password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- give all the user's properties to the database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Let the user see the perfomance data
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
