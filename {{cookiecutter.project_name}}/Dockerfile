# Debian base image
FROM python:3.12.6-slim-bookworm
RUN apt-get update && apt-get -y install gcc libpq-dev 
# libpq-dev is the PostgreSQL C API. It is only a couple hundred KBs so it
# is reasonable to add for when we inevitably need psycopg2 for Postgres.
RUN ls -la
RUN pip install --upgrade pip setuptools wheel
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/
