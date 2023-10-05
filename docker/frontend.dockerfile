FROM node:lts-alpine

WORKDIR /project

COPY ./frontend/package*.json ./

COPY ./frontend .

EXPOSE 5173