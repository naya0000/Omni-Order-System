#!/bin/sh

sh wait-for-postgres.sh db
python manage.py runserver 0.0.0.0:8008