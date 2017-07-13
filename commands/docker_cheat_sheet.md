#### Lsit docker machines
```
docker-machine ls
```
#### RUN DOCKER
```
$ docker-machine start [docker-machine]
```
#### SSH DOCKER MACHINE
```
$ docker-machine ssh default
```
#### Check running dockers
```
$ docker-machine env [docker-machine]
```
#### Start docker image with compose
```
$ cd ~/Project/[project_name]
$ docker-compose up
or
$ docker-compose up [docker-image-name]
```
#### List Docker containers
```
$ docker ps -a
```
```
docker-compose build no cache
docker-compose build --no-cache author
```
#### Mongoimport
```
mongoimport --drop -d test -c zips small_zips.json
```
#### List DB's
```
show dbs
```
