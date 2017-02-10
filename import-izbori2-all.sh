#!/bin/sh
source ./venv/bin/activate

python import-izbori.py --election predsjednicki --year 2004 --month juna --round drugi --granular
