#!/bin/sh
source ./venv/bin/activate

if [ "$#" -ne 1 ]
then
    echo "Invalid number of parameters."
else
    python importer.py
fi
