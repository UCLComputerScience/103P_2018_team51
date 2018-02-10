FROM alpine:latest
RUN apk add --no-cache \
  python3 \
  python3-dev \
  build-base \
  postgresql-dev \
  nodejs
RUN npm install gulp-cli -g
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip3 install -r requirements.txt
RUN npm install
