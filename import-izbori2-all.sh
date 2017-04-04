#!/bin/sh
source ./venv/bin/activate

#parlamentarni

python import-izbori.py --election parlamentarni --year 2016 --granular
