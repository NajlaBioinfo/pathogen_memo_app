FROM python:3.8.1-buster
# Created with : "Debian GNU/Linux 10 (buster)"
# LABEL 'PathogenMemo web app One Container strategyi(dev).'
# By Najlabioinfo JAN 2020

LABEL maintainer="bhndevtools@gmail.com"

# Update
RUN apt-get update -y
RUN apt-get -y upgrade
RUN apt-get install sudo vim tree curl wget -y
RUN sudo apt-get install libpq-dev -y 

# Install Git
RUN apt-get install git less -y
RUN sudo sh -c "curl https://raw.githubusercontent.com/mrowa44/emojify/master/emojify -o /usr/local/bin/emojify && chmod +x /usr/local/bin/emojify"

# Install python 3.8.1
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8


RUN sudo apt-get install build-essential -y
RUN sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev -y

RUN apt-get update && apt-get install -y --no-install-recommends \
		libbluetooth-dev \
		tk-dev \
		uuid-dev \
	&& rm -rf /var/lib/apt/lists/*


RUN python3.8 -V



#INSTALL POSTGRES
RUN apt-get update -y
RUN apt-get -y upgrade
RUN sudo apt-get install postgresql postgresql-contrib postgresql-client -y
RUN sudo apt-get install python-psycopg2 -y

#INSTAL NGNIX
RUN sudo apt-get install nginx -y
RUN cd /etc/nginx/sites-available
ADD . flaskconfig 
RUN cd /etc/nginx/sites-enabled
#RUN sudo ln -s ../sites-available/flaskconfig .
#RUN sudo rm default



EXPOSE 5000
EXPOSE 8080
EXPOSE 5432
EXPOSE 1337


RUN pip3 install virtualenv
RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

RUN python3 -m virtualenv --python=/usr/bin/python3 /opt/venv
RUN . /opt/venv/bin/activate


WORKDIR /najlabioinfo/pathogenMemoPackage/

## App requirements
ADD ./requirements.txt /najlabioinfo/pathogenMemoPackage/requirements.txt
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt


ADD . /najlabioinfo/pathogenMemoPackage/


RUN chmod +x ini.sh

#CMD sh ini.sh && flask run --host=0.0.0.0 --port=5000
CMD sh ini.sh