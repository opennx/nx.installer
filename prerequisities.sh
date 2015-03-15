#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

#
# Install base prerequisities
#

apt-get -y install git build-essential
apt-get -y install python-psycopg2 libyaml-dev python-pip python-dev
apt-get -y install python-cairo python-gtk2 python-imaging

pip install flask flask-login pyyaml

#
# Parse command line options
#

nginx=0
ffmpeg=0

while getopts "nf" opt; do
    case "$opt" in
    n)  
        install_nginx=1
        ;;
    f)  
        install_ffmpeg=1
        ;;
    esac
done

shift $((OPTIND-1))
[ "$1" = "--" ] && shift


[ ! -d src/ ] && mkdir src/
cd src/

#
# FFMPEG
#

if [ $install_ffmpeg ]; then
    echo "Installing ffmpeg..."
    if [ ! -f /usr/local/bin/ffmpeg ]; then
        [ ! -f inst.ffmpeg.sh ] && (wget https://raw.githubusercontent.com/opennx/broadcast-tools/master/inst.ffmpeg.sh || exit 1)
        chmod +x inst.ffmpeg.sh
        ./inst.ffmpeg.sh
    fi

fi

#
# NGINX
#

if [ $install_nginx ]; then
    echo "Installing nginx..."
    if [ ! -f /opt/nginx/sbin/nginx ]; then
        [ ! -f inst.nginx.sh ] && (wget https://raw.githubusercontent.com/opennx/broadcast-tools/master/inst.nginx.sh || exit 1)
        chmod +x inst.nginx.sh
        ./inst.nginx.sh
    fi

    echo "Creating SSL key..."
    if [ ! -f /opt/nginx/cert/nginx.pem ]; then
        mkdir /opt/nginx/cert
        openssl req -new -x509 -days 365 -nodes -out /opt/nginx/cert/nginx.pem -keyout /opt/nginx/cert/nginx.key
    fi

fi

