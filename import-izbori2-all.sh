#!/bin/sh
source ./venv/bin/activate
python import-izbori.py --election parlamentarni --year 2003 --granular

python import-izbori.py --election predsjednicki --year 2003 --month november --round drugi --granular

