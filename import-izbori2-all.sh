#!/bin/sh
source ./venv/bin/activate

python import-izbori.py --election parlamentarni --year 2003 --granular
python import-izbori.py --election parlamentarni --year 2007 --granular
python import-izbori.py --election parlamentarni --year 2008 --granular
python import-izbori.py --election parlamentarni --year 2012 --granular
python import-izbori.py --election parlamentarni --year 2014 --granular
python import-izbori.py --election parlamentarni --year 2016 --granular

python import-izbori.py --election predsjednicki --year 2002 --month decembar --round prvi --granular
python import-izbori.py --election predsjednicki --year 2002 --month decembar --round drugi --granular

python import-izbori.py --election predsjednicki --year 2003 --month november --round drugi --granular

python import-izbori.py --election predsjednicki --year 2004 --month juna --round prvi --granular
python import-izbori.py --election predsjednicki --year 2004 --month juna --round drugi --granular

python import-izbori.py --election predsjednicki --year 2008 --month januar --round prvi --granular
python import-izbori.py --election predsjednicki --year 2008 --month februari --round drugi --granular

python import-izbori.py --election predsjednicki --year 2012 --month maja --round prvi --granular
python import-izbori.py --election predsjednicki --year 2012 --month maja --round drugi --granular