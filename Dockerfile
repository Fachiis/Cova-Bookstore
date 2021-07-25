# Pull base image
FROM python:3.9

# Set envirnoment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /django_docker

# Install dependencies
COPY Pipfile Pipfile.lock /django_docker/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /django_docker/
