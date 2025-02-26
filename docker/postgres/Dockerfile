FROM postgres:17.2

COPY ./docker/postgres/sql/migration /docker-entrypoint-initdb.d
COPY ./docker/postgres/sql/demo /docker-entrypoint-initdb.d
