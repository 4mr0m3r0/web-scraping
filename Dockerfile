FROM python:3.9.0-buster
MAINTAINER Romero

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./ /app

RUN adduser --disabled-login user
USER user
