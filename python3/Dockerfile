FROM python:3

RUN apt-get update

ADD . /src
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
