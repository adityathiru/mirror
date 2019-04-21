FROM ubuntu:16.04

RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise main restricted universe multiverseoutput = json\n\
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-updates main restricted universe multiverse\n\
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-backports main restricted universe multiverse\n\
deb mirror://mirrors.ubuntu.com/mirrors.txt precise-security main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get clean && apt-get update --fix-missing && \
    apt-get install -y  build-essential \
                        git \
                        python2.7 \
                        python2.7-dev \
                        python-setuptools \
                        bcrypt \
                        libssl-dev \
                        libffi-dev \
                        libpq-dev \
                        vim \
                        rsyslog \
                        wget \
                        unzip \
                        libxss1 \
                        libappindicator1 \
                        libindicator7 \
                        xvfb \
                        gconf-service \
                        libasound2 \
                        libgconf-2-4 \
                        libnspr4 \
                        fonts-liberation \
                        libnss3 \
                        xdg-utils \
                        libxml2-dev \
                        libxslt1-dev \
                        python-dev \
                        lsb-release \
                        tcl \
                        tk \
                        curl

RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:jonathonf/python-3.6
RUN apt-get update && \
    apt-get install -y build-essential \
                        python3.6 \
                        python3.6-dev \
                        python3-pip \
                        python3.6-venv

RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.6 /usr/bin/python3
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.6 /usr/bin/python

RUN pip3 install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 install -r /app/requirements.txt

CMD python /app/api.py