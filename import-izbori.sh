#!/bin/sh
source ./venv/bin/activate

if [ "$#" -ne 2 ]
then
    echo "Invalid number of parameters."
else
    python import-izbori.py --election $1 --year $2
fi
