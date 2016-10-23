#!/bin/sh
source ./venv/bin/activate

python import-izbori.py --election parlamentarni --year 2000
python import-izbori.py --election parlamentarni --year 2003
python import-izbori.py --election parlamentarni --year 2007
python import-izbori.py --election parlamentarni --year 2008
python import-izbori.py --election parlamentarni --year 2012
python import-izbori.py --election parlamentarni --year 2014
python import-izbori.py --election parlamentarni --year 2016

python import-izbori.py --election predsjednicki --year 2002 --month septembar --round prvi
python import-izbori.py --election predsjednicki --year 2002 --month oktobar --round drugi
python import-izbori.py --election predsjednicki --year 2002 --month decembar --round prvi
python import-izbori.py --election predsjednicki --year 2003 --month novembar --round prvi
python import-izbori.py --election predsjednicki --year 2004 --month jun --round prvi
python import-izbori.py --election predsjednicki --year 2004 --month jun --round drugi
python import-izbori.py --election predsjednicki --year 2008 --month januar --round prvi
python import-izbori.py --election predsjednicki --year 2008 --month februar --round drugi
python import-izbori.py --election predsjednicki --year 2012 --month maj --round prvi
python import-izbori.py --election predsjednicki --year 2012 --month maj --round drugi


