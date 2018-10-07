## Pre-requires

1. install Docker

## Develop

Run app in docker:  

```bash
$ docker-compose up
```

List docker containers:    

```bash
$ docker ps
```

Login in Redis:  

```bash
docker exec -it ${redis_container_id} redis-cli
```

Run app in local:

1. Change Code:

```bash
DB_HOST = 'redis'
```
to 

```bash
DB_HOST = 'localhost'
```

```bash
$ docker-compose up redis
$ export FLASK_ENV=development
$ flask run
```
