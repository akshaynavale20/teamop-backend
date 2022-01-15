#!/bin/bash -e
if [ "requirements.txt" -nt "venv/.localdev-venv" ] ; then
    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt --no-chache
    sed 's/psycopg2/psycopg2-binary/g' requirements.txt | ./venv/bin/pip install --no-deps -r /dev/stdin
    touch -r requirements.txt venv/.localdev-venv
fi
