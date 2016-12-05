#!/bin/sh
source ./venv/bin/activate
python import-izbori.py --election parlamentarni --year 2012 --granular
python import-izbori.py --election parlamentarni --year 2014 --granular
python import-izbori.py --election parlamentarni --year 2016 --granular


