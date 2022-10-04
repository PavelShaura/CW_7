FROM python:3.10

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /usr/src/app
COPY . .

CMD python manage.py runserver 0.0.0.0:8000