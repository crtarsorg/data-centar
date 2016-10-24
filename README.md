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

Import data for 2016 Parliamentary Election:

`bash import-izbori.sh parlamentarni 2016`

Import data for 2008 first round Presidential Election:

`bash import-izbori.sh predsjednicki 2008 januar prvi`

Import all election data:

`bash import-izbori-all.sh`


## API
### Budzet
TODO: Document

### Elections
#### Parliamentary
**GET** election results grouped by territories:

/api/izbori/parlamentarni/godina/&lt;int:godina&gt;/teritorija

**GET** election results for a given territory:

/api/izbori/parlamentarni/godina/&lt;int:godina&gt;/teritorija/&lt;string:territory_slug&gt;

**GET** election results grouped by parties:

/api/izbori/parlamentarni/godina/&lt;int:godina&gt;/izborna-lista

**GET** election results for a given party:

/api/izbori/parlamentarni/godina/&lt;int:godina&gt;/izborna-lista/&lt;string:izborna_lista_slug&gt;

#### Presidential
Note: value of 'krug' parameter can be set to either 'prvi' or 'drugi'.

**GET** election results grouped by territories:

/api/izbori/predsjednicki/godina/&lt;int:godina&gt;/krug/&lt;string:krug&gt;/teritorija

**GET** election results for a given territory:

/api/izbori/predsjednicki/godina/&lt;int:godina&gt;/krug/&lt;string:krug&gt;/teritorija/&lt;string:teritorija_slug&gt;

**GET** election results grouped by candidates:

/api/izbori/predsjednicki/godina/&lt;int:godina&gt;/krug/&lt;string:krug&gt;/kandidat

**GET** election results for a given candidate:

/api/izbori/predsjednicki/godina/&lt;int:godina&gt;/krug/&lt;string:krug&gt;/kandidat/&lt;string:kandidat_slug&gt;
