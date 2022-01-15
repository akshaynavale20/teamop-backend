#!/bin/bash -e

./localvenvrefresh.sh
cd src
exec ../venv/bin/python3 manage.py runserver
