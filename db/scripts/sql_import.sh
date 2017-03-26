#!/bin/bash
mysql -u root -p'testing' inventory<<EOFMYSQL
GRANT ALL ON inventory.* TO 'bryggeriklubben'@'%';
LOAD DATA LOCAL INFILE '/docker-entrypoint-initdb.d/dummy_data.csv' INTO TABLE ingredients FIELDS TERMINATED BY ','  LINES TERMINATED BY '\n'  (name, description, alpha, amount, date, type)
EOFMYSQL