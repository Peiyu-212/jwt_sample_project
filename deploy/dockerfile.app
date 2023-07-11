##### Build Image
FROM python:3.7-slim-bullseye AS builder
LABEL maintainer Peiyu Jhong

RUN echo "deb http://opensource.nchc.org.tw/debian/ bullseye main" > /etc/apt/sources.list \
    && echo "deb http://opensource.nchc.org.tw/debian/ bullseye-updates main" >> /etc/apt/sources.list \
    && echo "deb http://opensource.nchc.org.tw/debian/ bullseye-proposed-updates main" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends\
    build-essential \
    libldap2-dev \
    #=2.4.47+dfsg-3+deb10u4 \
    libsasl2-dev \
    libpq-dev \
    libaio-dev

RUN apt-get install -y wget \
    unzip \
    libaio-dev \
    wget \
    libpq-dev \
    tzdata \
    cron \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

COPY ./backend /backend
COPY ./.env /.env
COPY ./backend/compose/requirements.txt /backend/requirements.txt

WORKDIR /backend

RUN pip install --upgrade pip
RUN pip install -r /backend/requirements.txt


### COPY the uwsgi configuration file
COPY ./deploy/uwsgi.ini /etc/uwsgi/uwsgi.ini
RUN mkdir -p  /log \
    && chown -R www-data:www-data /log
### Port to use with TCP proxy
EXPOSE 55555
### Start uWSGI on container startup
CMD ["/usr/local/bin/uwsgi", "--ini", "/etc/uwsgi/uwsgi.ini"]