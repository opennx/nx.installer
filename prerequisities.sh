#!/bin/bash

apt-get -y install python-psycopg2 python-pylibmc python-cairo python pip
pip install flask flask-login

mkdir src
cd src

if hash ffmpeg 2>/dev/null; then
    if [! -f inst.ffmpeg.sh ]; then
        wget https://raw.githubusercontent.com/opennx/broadcast-tools/master/inst.ffmpeg.sh
    fi 
    chmod +x inst.ffmpeg.sh
    ./inst.ffmpeg.sh
fi

if [! -f /opt/nginx/sbin/nginx]; then
    if [! -f inst.nginx.sh ]; then
        wget https://raw.githubusercontent.com/opennx/broadcast-tools/master/inst.nginx.sh
    fi 
    chmod +x inst.nginx.sh
    ./inst.nginx.sh
fi

if [! -f /opt/nginx/sbin/nginx]; then
    if [! -f inst.nginx.sh ]; then
        wget https://raw.githubusercontent.com/opennx/broadcast-tools/master/inst.nginx.sh
    fi 
    chmod +x inst.nginx.sh
    ./inst.nginx.sh
fi


if [! -f /opt/nginx/cert/nginx.pem]
    mkdir /opt/nginx/cert
    openssl req -new -x509 -days 365 -nodes -out /opt/nginx/cert/nginx.pem -keyout /opt/nginx/cert/nginx.key
fi
