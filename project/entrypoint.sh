#!/bin/sh


echo "Initializing PostgreSQL..."


while ! nc -z db 5432; do
	sleep 0.1
done

echo "Initizizing PostgresSQL complete"

exec "$@"
