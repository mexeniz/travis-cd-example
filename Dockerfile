FROM python:3.7

RUN pip install gunicorn==19.9.0 \
    flask==1.0.2 \
    pytest==4.3.1

WORKDIR /app
COPY . /app

RUN pytest

 