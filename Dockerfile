FROM python:2.7
RUN apt-get update
RUN apt-get install -y gettext
RUN rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/