FROM python:3

RUN apt-get -y update

RUN apt-get -y install python3

RUN apt-get -y install python3-pip

#RUN apt-get install -y python-pip python-dev

WORKDIR /app

RUN pip install Flask requests flask_mysqldb

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]