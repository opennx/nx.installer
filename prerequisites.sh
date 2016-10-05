#!/bin/bash
#
# Copyright (c) 2016 imm studios, z.s.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
##############################################################################
## COMMON UTILS

BASE_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
TEMP_DIR=/tmp/$(basename "${BASH_SOURCE[0]}")

function critical_error {
    printf "\n\033[0;31mInstallation failed\033[0m\n"
    cd ${BASE_DIR}
    exit 1
}

function finished {
    printf "\n\033[0;92mInstallation completed\033[0m\n"
    cd ${BASE_DIR}
    exit 0
}


if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   error_exit
fi

if [ ! -d $TEMP_DIR ]; then
    mkdir $TEMP_DIR || error_exit
fi

## COMMON UTILS
##############################################################################

function install_base {
    apt-get -y install git build-essential cifs-utils || return 1
    apt-get -y install python-psycopg2 python-pylibmc libyaml-dev python-pip python-dev || return 1
    apt-get -y install python-cairo python-gtk2 python-imaging || return 1
    pip install flask flask-login pyyaml || return 1
    pip install cherrypy jinja2 || return 1
}


function install_ffmpeg {
    wget -q https://raw.githubusercontent.com/immstudios/installers/master/install.ffmpeg.sh -O ${BASEDIR}/install.ffmpeg.sh || return 1
    chmod +x install.ffmpeg.sh
    ./install.ffmpeg.sh || (rm install.ffmpeg.sh && return 1)
    rm install.ffmpeg.sh
}


function install_nginx {
    critical_error
    # install manually?
}

#
# Install it
#

install_base || error_exit

while getopts "nf" opt; do
    case "$opt" in
    n)
        install_nginx
        ;;
    f)
        install_ffmpeg
        ;;
    esac
done

shift $((OPTIND-1))
[ "$1" = "--" ] && shift

finished

