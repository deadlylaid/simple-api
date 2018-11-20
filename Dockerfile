FROM ubuntu:16.04

RUN apt-get update
RUN apt-get upgrade -y

RUN set -ex \
    && apt-get install -y build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev openssl libffi-dev python3-dev python3-setuptools wget

RUN mkdir -p mkdir /tmp/Python37
WORKDIR /tmp/Python37

RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
RUN tar xvf Python-3.7.0.tar.xz

WORKDIR /tmp/Python37/Python-3.7.0
RUN ./configure --enable-optimizations
RUN make altinstall

RUN set -ex \
    && apt-get -y install git nginx

COPY . /sample-api/
WORKDIR /sample-api/

RUN pip3.7 install -e .

RUN chmod 777 run.sh

CMD '/sample-api/run.sh'
