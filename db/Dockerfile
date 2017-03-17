FROM mysql:latest
COPY ./inventory.sql /docker-entrypoint-initdb.d
COPY /scripts/dummy_data.csv /home/
COPY /scripts/sql_import.sh /home/