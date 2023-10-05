FROM python:3.11

LABEL authors="krukov"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# папка, в которой будет лежать весь проект, то есть и docker и server итд
WORKDIR /project

COPY ./requirements/requirements.txt .
RUN pip install -r requirements.txt

# копирование всего проекта внутрь контейнера, то есть возьмется все с уровня Makefile и положится в папку
# /project/...
COPY . .

EXPOSE 8000