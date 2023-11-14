FROM postgres:latest

ENV POSTGRES_DB petshop_crud
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD dcmrdb

COPY ./db_scripts/ /docker-entrypoint-initdb.d/
