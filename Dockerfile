FROM python:3

WORKDIR /usr/src/app

# COPY requirements.txt ./

COPY . .

RUN pip3 install -r requirements.txt

ENV DJANGO_ENV=prod
ENV DOCKER_CONTAINER=1

EXPOSE 8000

# CMD [ "pipenv", "install" ]
CMD [ "bash", "start.sh" ]
