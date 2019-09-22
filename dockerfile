FROM python:3
RUN apt-get install default-libmysqlclient-dev
COPY requirements.txt .
RUN pip3 install -r requirements.txt 
WORKDIR /sknfproject



