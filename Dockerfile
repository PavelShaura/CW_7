# start from an official message
FROM python:3.10-slim

# set work directory
WORKDIR /code

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

# define the command to run when starting the container
CMD python manage.py runserver 0.0.0.0:8000