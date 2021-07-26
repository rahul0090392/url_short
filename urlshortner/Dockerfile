# Pull base image
FROM python:3.8.3-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/urlshortner/

COPY ./requirements.txt /usr/src/urlshortner/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /usr/src/urlshortner/requirements.txt

RUN apt-get autoremove -y
RUN apt-get autoclean -y
RUN apt-get clean -y

# Copy project
COPY . /usr/src/urlshortner/core/

