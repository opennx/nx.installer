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

BASEDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
TEMPDIR=/tmp/$(basename "${BASH_SOURCE[0]}")

function error_exit {
    printf "\n\033[0;31mInstallation failed\033[0m\n"
    cd $BASEDIR
    exit 1
}

function finished {
    printf "\n\033[0;92mInstallation completed\033[0m\n"
    cd $BASEDIR
    exit 0
}


if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   error_exit
fi

if [ ! -d $TEMPDIR ]; then
    mkdir $TEMPDIR || error_exit
fi

## COMMON UTILS
##############################################################################

DB_USER=`support/parse_settings.py db_user`
DB_PASS=`support/parse_settings.py db_pass`
DB_NAME=`support/parse_settings.py db_name`
SCRIPT_PATH="/tmp/nebula.sql"

function install_postgres {
    wget -q https://raw.githubusercontent.com/immstudios/installers/master/install.postgres.sh -O ${BASEDIR}/install.postgres.sh || return 1
    chmod +x install.postgres.sh
    ./install.postgres.sh || (rm install.posgres.sh && return 1)
    rm install.postgres.sh
}

function create_user {
    echo "Creating DB user"
    echo "
        DROP DATABASE IF EXISTS ${DB_NAME};
        DROP USER IF EXISTS ${DB_USER};
        CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASS}';
    " > ${SCRIPT_PATH}
    su postgres -c "psql --file=${SCRIPT_PATH}" || return 1
    rm ${SCRIPT_PATH}
}

function create_db {
    echo "Creating DB"
    echo "
        DROP DATABASE IF EXISTS ${DB_NAME};
        CREATE DATABASE ${DB_NAME} OWNER ${DB_USER};
        CREATE EXTENSION IF NOT EXISTS unaccent;
    " > ${SCRIPT_PATH}
    su postgres -c "psql --file=${SCRIPT_PATH}" || return 1
    rm ${SCRIPT_PATH}
}

function create_schema {
    echo "Creating DB schema"
    export PGPASSWORD="${DB_PASS}";
    psql -h localhost -U ${DB_USER} ${DB_NAME} --file=${BASEDIR}/support/schema.sql || return 1
}


echo ""
echo ""


if [ -z $DB_USER ] || [ -z $DB_PASS ] || [ -z $DB_NAME ]; then
    echo ""
    echo "DB connection params unspecified"
    error_exit
fi

if !(service postgresql status > /dev/null); then
    echo "This script must run on the DB server."
    while true; do
        read -p "Do you wish to install Postgresql server now??" yn
        case $yn in
            [Yy]* ) install_postgres || error_exit; break;;
            [Nn]* ) error_exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
fi

create_user || error_exit
create_db || error_exit
create_schema || error_exit
finished
