#!/bin/bash

apt-get -y install python-psycopg2 python-pylibmc python-cairo python-pip
pip install flask flask-login


[ ! -d src/ ] && mkdir src/
cd src/

if hash ffmpeg 2>/dev/null; then
    [ ! -f inst.ffmpeg.sh ] && (wget https://raw.githubusercontent.com/opennx/broadcast-tools/master/inst.ffmpeg.sh || exit 1)
    chmod +x inst.ffmpeg.sh
    ./inst.ffmpeg.sh
fi

if [ ! -f /opt/nginx/sbin/nginx ]; then
    [ ! -f inst.nginx.sh ] && (wget https://raw.githubusercontent.com/opennx/broadcast-tools/master/inst.nginx.sh || exit 1)
    chmod +x inst.nginx.sh
    ./inst.nginx.sh
fi


if [ ! -f /opt/nginx/cert/nginx.pem ]; then
    mkdir /opt/nginx/cert
    openssl req -new -x509 -days 365 -nodes -out /opt/nginx/cert/nginx.pem -keyout /opt/nginx/cert/nginx.key
fi

