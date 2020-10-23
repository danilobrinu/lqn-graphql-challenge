FROM python:3.7-alpine as builder
ENV PYTHONUNBUFFERED 1
RUN apk --no-cache add build-base mariadb-dev gcc jpeg-dev zlib-dev
WORKDIR /app
COPY . requirements.production /app/
RUN pip install -r requirements.production

FROM builder
WORKDIR /app
COPY . .
ENTRYPOINT ["python", "run.py"]
