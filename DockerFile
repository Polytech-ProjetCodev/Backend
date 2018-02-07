FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install pipenv

COPY . .

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

CMD [ "pipenv", "install" ]
CMD [ "pipenv", "run gunicorn backendDjango.wsgi:application --bind 0.0.0.0:8000 --workers 3" ]
