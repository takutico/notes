RUN DOCKER
```
>>> docker-machine start default
```
SSH DOCKER MACHINE
```
>>> docker-machine ssh default
```
Check running dockers
```
>>> docker-machine env default
```
Start docker image with compose
```
>>> cd ~/Project/[project_name]
>>> docker-compose up
or
>>> docker-compose up [docker-image-name]
```
List Docker containers
```
>>> docker ps -a
```
docker-compose build no cache
docker-compose build --no-cache author