# DataCentar

## Install
`bash install.sh`

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

Import 2016 Parliamentary Election data:
`bash import-izbori.sh parlamentarni 2016`

Import 2014 Presidential Election data:
`bash import-izbori.sh predsjednicki 2014`

Import all election data:
`bash import-izbori-all.sh`


## API
### Budzet
TODO: Document

### Elections
**GET** election results grouped by territories:
/api/izbori/<string:election_type_slug>/godina/<int:year>/teritorija

**GET** election results for a given territory:
/api/izbori/<string:election_type_slug>/godina/<int:year>/teritorija/<string:territory_slug>

**GET** election results grouped by parties:
/api/izbori/<string:election_type_slug>/godina/<int:year>/izborna-lista

**GET** election results for a given party:
/api/izbori/<string:election_type_slug>/godina/<int:year>/izborna-lista/<string:izborna_lista_slug>

