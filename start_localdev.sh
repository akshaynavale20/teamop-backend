#!/bin/bash -e
[ "$1" == "" ] && echo "Please specify runserver, makemigrations, migrate as an argument to this script" && exit 1
./localvenvrefresh.sh
cd src
exec ../venv/bin/python manage.py $1
