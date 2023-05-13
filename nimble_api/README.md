# Nimble API

[![Deploy](https://github.com/.../actions/workflows/deploy.yml/badge.svg)](https://github.com/.../actions/workflows/deploy.yml)

## Init

##### Destroy docker containers and volumes
```bash
docker system prune -a
docker volume prune
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```

##### Docker (dev)
```bash
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py loaddata initial_data
docker-compose run web python3 manage.py makemessages -l ru
docker-compose run web python3 manage.py makemessages -l en
docker-compose run web python3 manage.py compilemessages -l ru
docker-compose run web python3 manage.py compilemessages -l en
docker-compose run web python3 manage.py createsuperuser
docker-compose build --no-cache
docker-compose up
```

##### Docker (production)
```bash
docker-compose -f docker-compose.prod.yml run web python3 manage.py makemigrations
docker-compose -f docker-compose.prod.yml run web python3 manage.py migrate
docker-compose -f docker-compose.prod.yml run web python3 manage.py loaddata initial_data
docker-compose -f docker-compose.prod.yml run web python3 manage.py dumpdata socialaccount > nimble/common/fixtures/initial_data.json
docker-compose -f docker-compose.prod.yml run web python3 manage.py createsuperuser
docker-compose -f docker-compose.prod.yml build --no-cache
docker-compose -f docker-compose.prod.yml up
```


##### .env file
```bash
DEBUG=True
SECRET_KEY==change_me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_HOST=db
HTTPS=False
```
