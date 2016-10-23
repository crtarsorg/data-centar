#!/bin/sh
source ./venv/bin/activate
if [ "$#" -eq 2 ]
then
    python import-izbori.py --election $1 --year $2
elif [ "$#" -eq 4 ]
then
    python import-izbori.py --election $1 --year $2 --month $3 --round $4
fi
