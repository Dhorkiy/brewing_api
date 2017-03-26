FROM mysql:latest
COPY ./inventory.sql /docker-entrypoint-initdb.d
COPY /scripts/dummy_data.csv /docker-entrypoint-initdb.d/
COPY /scripts/sql_import.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/sql_import.sh