# Docker Demo #

**Run using docker-compose**

```bash
$ docker-compose up --build
```

Go to : http://localhost:8080/

**Run using docker**

*Build the backend using the following command.*

```bash
$ cd backend
$ docker build -t python-backend .
$ docker run -d -p 5000:5000 --name python-backend-running python-backend
```

Below commands can be helpful in debugging
```bash
$ docker ps -a
$ docker container exec -it python-backend-running /bin/bash
docker container attach 
$ docker logs python-backend-running
$ docker stop python-backend-running
$ docker start python-backend-running
$ docker rm python-backend-running
```

*Build the frontend using the following command.*

```bash
$ cd backend
$ docker build -t nginx-frontend .
$ docker run -d -p 8080:80 --name nginx-frontend-running nginx-frontend
```

Go to : http://localhost:8080/