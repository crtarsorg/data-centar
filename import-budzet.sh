#!/bin/sh
source ./venv/bin/activate

if [ "$#" -ne 2 ]
then
    echo "Invalid number of parameters."
else
    python import-budzet.py --data $1 --municipalities $2
fi
