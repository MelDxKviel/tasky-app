#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate --no-input
gunicorn config.wsgi -c ./config/gunicorn.py