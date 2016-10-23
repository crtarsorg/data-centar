#!/bin/sh
source ./venv/bin/activate

python import-izbori.py --election parlamentarni --year 2000
python import-izbori.py --election parlamentarni --year 2003
python import-izbori.py --election parlamentarni --year 2007
python import-izbori.py --election parlamentarni --year 2008
python import-izbori.py --election parlamentarni --year 2012
python import-izbori.py --election parlamentarni --year 2014
python import-izbori.py --election parlamentarni --year 2016

