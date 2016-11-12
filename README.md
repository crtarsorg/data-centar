# DataCentar

## Install

`bash install.sh`

## Configure
Create configuration file and set config property values:

```
cp config-template.cfg config.cfg
nano config.cfg
```

## Run
`bash run.sh`

For debug mode:

`bash run-debug.sh`

## Importing Data
### Budget Data

Import prihodi and rashodi data for all municipalities:

`bash import-budzet.sh prihodi,rashodi all`

Import prihodi data for the municipalities of Vranja:

`bash import-budzet.sh prihodi vranje`

Import rashodi data for the municipalities of Vranja and Novi Beograd:

`bash import-budzet.sh rashodi vranje,novi_beograd`

Data is available for the following municipalities:

- prijepolje
- vranje
- loznica
- sombor
- valjevo
- indjija
- cacak
- kraljevo
- zvezdara
- novi_beograd

### Election Data
#### Data Source: Statistical Agency

Import data for 2016 Parliamentary Election:

`bash import-izbori.sh parlamentarni 2016`

Import data for 2008 first round Presidential Election:

`bash import-izbori.sh predsjednicki 2008 januar prvi`

Import all election data:

`bash import-izbori-all.sh`

#### Data Source: CRTA Spreadsheets
Currently only available for 2014 and 2016 parliamentary elections.

Import all election data:

`bash import-izbori2-all.sh`


## API
### Budzet
TODO: Document

### Elections
We have two data sources for election data:
1 - Statistics Agency: Covers parliamentary elections from 2000 to 2016 and presidential electiosn from 2002 to 2012.
2 - CRTA Spreadsheets: Only covers parliamentary elections for 2014 and 2016. Has more data than Statistics Agency such as valid/invalid ballots, other ballot information, and polling stations addresses (as well as coordinates for 2016).

#### Parliamentary
##### Some notes on two URL parameters:

**data_source_id**
The value of data_source_id can either be **1**, to fetch data from Statistics Agency, or **2**, to fetch data from CRTA Spreadsheet.
Using data_source_id **2** is currently only available for 2014 and 2016 parliamentary elections when disaggregating by territory.
All other requests with Data Source **2** have not yet been implemented

**territory_admin_level**
The value of territory_admin_level can be from 1 to 4. The higher the number to more granular the territorial area we are retrieving data from.

1: Large aggregation of territories that include several municipalities or counties. E.g.: "Vojvodina" or even just all of "Republic of Serbia."
2: Counties (Okrug). E.g.: "Nisavski Okrug," "Rasinski Okrug," or even "Grad Beograd."
3: Municipalities. E.g.: "Senta" or  "Plandiste."
4: Polling Stations.

Data Source 1 only supports requests from 1 through 3 for all election types and all years.
Data Source 2 supports from 1 through 4 but only for 2014 and 2016 parliamentary elections.

Requests for territory_admin_level **4** for Data Source 2 might return an error due to the large size of the response it generates. THis is because it attempts to fetch results disaggregated by  polling station and there are a lot of polling stations.
**This needs to be fixed, probably with pagination.**

##### The API Requests

**GET** election results grouped by territories:

/api/izbori/&lt;int:data_source_id&gt;/parlamentarni/godina/&lt;int:godina&gt;/teritorija/instanca/&lt;int:territory_admin_level&gt;

_Note: Works with Data Source 2._

**GET** election results for a given territory:

/api/izbori/&lt;int:data_source_id&gt;/parlamentarni/godina/&lt;int:godina&gt;/teritorija/instanca/&lt;int:territory_admin_level&gt;/&lt;string:territory_slug&gt;

_Note: Works with Data Source 2._

**GET** election results grouped by parties:

/api/izbori/&lt;int:data_source_id&gt;/parlamentarni/godina/&lt;int:godina&gt;/izborna-lista

_Note: Does not work with Data Source 2._

**GET** election results for a given party:

/api/izbori/&lt;int:data_source_id&gt;/parlamentarni/godina/&lt;int:godina&gt;/izborna-lista/&lt;string:izborna_lista_slug&gt;

_Note: Does not work with Data Source 2._

#### Presidential
Note: 
- Value of 'krug' parameter can be set to either 'prvi' or 'drugi'.
- None of these requests currently work with Data Source 2.

**GET** election results grouped by territories:

/api/izbori/&lt;int:data_source_id&gt;/predsjednicki/godina/&lt;int:godina&gt;/krug/&lt;string:krug&gt;/teritorija

**GET** election results for a given territory:

/api/izbori/&lt;int:data_source_id&gt;/predsjednicki/godina/&lt;int:godina&gt;/krug/&lt;string:krug&gt;/teritorija/&lt;string:teritorija_slug&gt;

**GET** election results grouped by candidates:

/api/izbori/&lt;int:data_source_id&gt;/predsjednicki/godina/&lt;int:godina&gt;/krug/&lt;string:krug&gt;/kandidat

**GET** election results for a given candidate:

/api/izbori/&lt;int:data_source_id&gt;/predsjednicki/godina/&lt;int:godina&gt;/krug/&lt;string:krug&gt;/kandidat/&lt;string:kandidat_slug&gt;
