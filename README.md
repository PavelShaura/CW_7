#step-by-step PROJECT
## PYTHON DEVELOPER FROM COURSE SKYPRO
Powered by Django framework, Postgres DB.

## How to launch project in development environment:

**1. Create virtual environment**

**2. Install dependencies from requirements.dev.txt**

> pip install -r todolist/requirements.dev.txt
> 
**3. Set environment variables in .env file**

> create .env file in todolist folder
> 
**you can copy the default variables from todolist/.env.example**

**4. Launch database from deploy folder**

> cd deploy
> 
>docker compose --env-file ../todolist/.env -f docker-compose.db.yaml up -d
> 
**5. Make migrations from todolist folder**

> cd todolist
> 
>./manage.py makemigraitons
> 
>./manage.py migrate
> 
**6. Launch project**
> 
> ./manage.py runserver
> 
##Accessing admin site**

**1. Create admin-user**

> ./manage.py createsuperuser
> 
set values and required fields

**2. Access admin site at http://127.0.0.1:8000/admin/**

##How to launch project in development with Docker-compose

**1. Create .docker_env file in deploy folder:**

***you can copy the default variables from todolist/.env.example
make sure to set DB_HOST to db which is a container name***

**2. Use docker-compose.dev.yaml from within deploy folder**

> cd deploy
> 
>docker compose --env-file .docker_env -f docker-compose.dev.yaml up -d
>

**3. The following would be done:**

***postgresql container would start
migrations would apply
api container would start
front container would start***

##Deploy

**1. Deploy is automated with github actions.**

**2. Project files used:**

***actions: .github/workflows/actions.yaml
compose file: deploy/docker-compose.ci.yaml
env variables: deploy/.ci_env
variables in compose and env files are replaced with github secrets***

**3. Docker hub images:**

***front: sermalenk/skypro-front:lesson-34
back: pshaura/todolist_project:***

**4. To add admin during first launch:**

***connect to server and access project folder***

> docker exec -it <api container_id> /bin/bash
> 
> ./manage.py createsuperuser
> 

**5. Addresses:**

> front: http://coder.pp.ru/auth
admin: http://coder.pp.ru/admin/
