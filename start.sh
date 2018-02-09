echo Starting Gunicorn.
exec gunicorn backendDjango.wsgi:application \
    --bind 163.172.159.182:8000 \
    --workers 3
