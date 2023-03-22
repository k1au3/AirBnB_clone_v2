-- script that prepares mysql server for project

-- Create a database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a user of the database and password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- give all the user's properties to the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Let the user see the perfomance data
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
