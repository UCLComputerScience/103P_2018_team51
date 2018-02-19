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
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD package.json /code/
ADD package-lock.json /code/
RUN npm install
ADD . /code/
RUN ls -Al node_modules
