#!/usr/bin/env bash
echo Starting Migration
python manage.py migrate

echo Starting Gunicorn.
exec gunicorn backendDjango.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
