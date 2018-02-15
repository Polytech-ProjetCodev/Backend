#!/bin/bash

host="163.172.159.182"
user="root"
workdir="/home/codev/"

docker build . --tag python4tw/web
docker push python4tw/web

ssh ${user}@${host} mkdir ${workdir} -p
scp docker-compose.yml ${user}@${host}:${workdir}

ssh ${user}@${host} "cd ${workdir}; docker-compose pull"
ssh ${user}@${host} "cd ${workdir}; docker-compose down"
ssh ${user}@${host} "cd ${workdir}; docker-compose up -d"

exit
