FROM ubuntu:latest

LABEL maintainer="Sidney Loyola"

RUN apt-get -y update

RUN apt-get -y install python3

RUN apt-get -y install vim

RUN apt-get -y install python3-pip

RUN apt-get -y install ffmpeg

RUN apt-get -y install vlc

RUN apt-get -y install sudo

RUN sudo sed -i 's/geteuid/getpid/' /usr/bin/vlc

RUN apt-get -y install pulseaudio

RUN apt-get -y install net-tools

RUN apt-get -y install iproute2

RUN apt-get -y install git

RUN apt-get install -y iputils-ping

RUN pip3 install git+https://github.com/itu-p1203/itu-p1203

WORKDIR /app/

COPY versao.txt /app

COPY qoe_meter.py /app



CMD ["python3","qoe_meter.py"]







