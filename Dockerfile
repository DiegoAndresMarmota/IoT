FROM python:3.11
ENV PYTHONUNBUFFERED 1
LABEL maintainer="Diego <diegoechalarp@hotmail.com>"

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000

