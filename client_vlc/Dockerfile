FROM ubuntu:latest

LABEL maintainer="Sidney Loyola"

RUN apt-get -y update

RUN apt-get -y install sudo

RUN apt-get -y install python3

RUN apt-get -y update

RUN apt-get -y install python3-pip

RUN apt-get -y install vim

RUN apt-get -y install ffmpeg

RUN apt-get -y install vlc

RUN sudo sed -i 's/geteuid/getpid/' /usr/bin/vlc

RUN apt-get -y install pulseaudio

RUN apt-get -y install net-tools

RUN apt-get -y install iproute2

RUN apt-get install -y iputils-ping

WORKDIR /app/

COPY qoe_meter.py /app

COPY teste_instalacao_itup1203.py /app

COPY itu-p1203-master /app

CMD ["python3","teste_instalacao_itup1203.py"]







