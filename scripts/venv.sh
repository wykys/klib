#!/usr/bin/env bash
# create and install python enviroment
# wykys 2018

if [ $1 = "update" ]; then
    echo "RM"
if

if [ -d ".venv" ]; then
    echo "venv exist"

    echo "activate venv"
    . .venv/bin/activate
else
    echo "create new venv"
    python3 -m venv .venv

    echo "activate venv"
    . .venv/bin/activate

    echo "upgrade pip"
    pip install --upgrade pip

    echo "install modules from requirements"
    pip install -r requirements.txt

    echo "installed modules"
    pip freeze
fi

echo $1
