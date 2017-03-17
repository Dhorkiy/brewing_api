#!/bin/bash
mysql -u root -p'testing' inventory<<EOFMYSQL
LOAD DATA LOCAL INFILE 'dummy_data.csv' INTO TABLE ingredients FIELDS TERMINATED BY ','  LINES TERMINATED BY '\n'  (id, name, description, alpha, amount, date, type)
EOFMYSQL