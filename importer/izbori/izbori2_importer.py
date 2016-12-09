# coding=utf-8
from flask_pymongo import MongoClient
import cyrtranslit
from slugify import slugify
from tqdm import tqdm
import csv


# Instantiate mongo client
mongo = MongoClient()

# Create mongo database instance
db = mongo['datacentar']
collection = 'izbori2'
class Izbori2DataImporter(object):

    def import_data(self, election_type, year, month=None, rnd=None):
        if election_type == 'parlamentarni' and int(year) == 2016:
            self.import_data_parliament_2016()
        elif election_type == 'parlamentarni' and int(year) == 2008:
            self.import_data_parliament_2008()
        elif election_type == 'parlamentarni' and int(year) == 2007:
            self.import_data_parliament_2007()
        else:
            self.import_data_rest(election_type, year, month, rnd)

    def import_data_parliament_2007(self):
        election_type = 'parlamentarni'
        year = 2007
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in range(12, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '')
                else:
                    territory = row[2].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                    polling_station_num = int(row[3].strip())
                    polling_station_address = row[4].strip()
                    ballots_received_count = int(row[5].strip())
                    unused_ballots_count = int(row[6].strip())
                    number_of_voters_registered=int(row[7].strip())
                    voters_who_voted_count = int(row[8].strip())
                    ballots_in_ballot_box_count = int(row[9].strip())
                    invalid_ballots_count = int(row[10].strip())
                    valid_ballots_count = int(row[11].strip())


                    doc['brojPrimljeniGlasackiListica'] = ballots_received_count
                    doc['brojNeupotrebljenihGlasackiListica']=unused_ballots_count
                    doc['brojBiracaUpisanihUBirackiSpisak'] = number_of_voters_registered
                    doc['nevazeciGlasackiListici']= invalid_ballots_count
                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = ballots_in_ballot_box_count
                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count

                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug \
                            or territory_slug in ['grad-beograd', 'inostranstvo'] \
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address
                    total_votes=0
                    udeo=0
                    for j in range(12, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])
                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / total_votes) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo
                        doc['teritorija'] = territory
                        doc['teritorijaSlug'] = territory_slug
                        doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                        doc['godina'] = int(year)

                        doc['izbornaLista'] = candidates_or_parties[str(j)]

                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)

    def import_data_parliament_2008(self):
        election_type = 'parlamentarni'
        year = 2008
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in xrange(10, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                elif row_count == 1:
                    pass

                else:
                    territory = row[0].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                    polling_station_num = int(row[1].strip()) if row[1].strip() is not '' else row[1].strip()
                    polling_station_address = row[2].strip()
                    ballots_received_count = int(row[3].strip())
                    unused_ballots_count = int(row[4].strip())
                    number_of_voters_registered=int(row[5].strip())
                    ballots_in_ballot_box_count = int(row[6].strip())
                    invalid_ballots_count = int(row[7].strip())
                    valid_ballots_count = int(row[8].strip())
                    voters_who_voted_count=int(row[9].strip())

                    doc['brojPrimljeniGlasackiListica'] = ballots_received_count
                    doc['brojNeupotrebljenihGlasackiListica']=unused_ballots_count
                    doc['brojBiracaUpisanihUBirackiSpisak'] = number_of_voters_registered
                    doc['nevazeciGlasackiListici']= invalid_ballots_count
                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = ballots_in_ballot_box_count
                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count

                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug \
                            or territory_slug in ['grad-beograd', 'inostranstvo'] \
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'),
                                                              to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address
                    total_votes=0
                    udeo=0
                    for j in range(10, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])
                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / total_votes) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo
                        doc['teritorija'] = territory
                        doc['teritorijaSlug'] = territory_slug
                        doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                        doc['godina'] = int(year)

                        doc['izbornaLista'] = candidates_or_parties[str(j)]

                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)


    def import_data_parliament_2016(self):
        election_type = 'parlamentarni'
        year = 2016
        self.prep_import(election_type, year, None, None)
        file_path = self.get_data_file_path(election_type, year, None, None)
        row_count = 0
        docs = []
        candidates_or_parties = {}
        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    for i in range(14, len(row)):
                        candidates_or_parties[str(i)] = row[i].replace('\n', '')

                elif row[7].strip() is not '':  # FIXME: we do this because row 8,350 is blank.
                    parent_territory = row[1].strip()
                    parent_territory_slug = slugify(cyrtranslit.to_latin(parent_territory, 'sr'), to_lower=True)

                    territory = row[3].strip()
                    territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)

                    polling_station_num = int(row[4].strip())
                    polling_station_address = row[5].strip()
                    coordinates = row[6].strip().split(',')

                    registered_voters_count = int(row[7].strip())
                    ballots_received_count = int(row[8].strip())
                    unused_ballots_count = int(row[9].strip())

                    voters_who_voted_count = int(row[10].strip())
                    # voters_who_voted_percent = None

                    ballots_in_ballot_box_count = int(row[11].strip())

                    invalid_ballots_count = int(row[12].strip())
                    # invalid_ballots_percent = None

                    valid_ballots_count = int(row[13].strip())
                    # valid_ballots_percent = None

                    # Set election type and year
                    doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                    doc['godina'] = int(year)

                    # Set generic location values
                    doc['teritorija'] = territory
                    doc['teritorijaSlug'] = territory_slug

                    doc['parentTeritorija'] = parent_territory
                    doc['parentTeritorijaSlug'] = parent_territory_slug

                    doc['brojBirackogMesta'] = polling_station_num
                    doc['adresaBirackogMesta'] = polling_station_address

                    # FIXME: at least one coordinate is missing (row 1481)
                    if len(coordinates) == 2:
                        doc['koordinateBirackomMestu'] = {}
                        doc['koordinateBirackomMestu']['latituda'] = float(coordinates[0].strip())
                        doc['koordinateBirackomMestu']['longituda'] = float(coordinates[1].strip())

                    # Set generic ballot values
                    doc['brojUpisanihBiracaUBirackiSpisak'] = registered_voters_count

                    doc['biraciKojiSuGlasali'] = {}
                    doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count
                    # doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent

                    doc['brojPrimljenihGlasackihListica'] = ballots_received_count
                    doc['brojNeupoTrebljenihGlasackihListica'] = unused_ballots_count
                    doc['brojGlasackihListicaUKutiji'] = ballots_in_ballot_box_count

                    doc['brojGlasackihListicaUKutiji'] = {}
                    doc['brojGlasackihListicaUKutiji']['broj'] = invalid_ballots_count
                    # doc['brojGlasackihListicaUKutiji']['udeo'] = invalid_ballots_percent

                    doc['vazeciGlasackiListici'] = {}
                    doc['vazeciGlasackiListici']['broj'] = valid_ballots_count
                    # doc['vazeciGlasackiListici']['udeo'] = valid_ballots_percent

                    # For this year, we don't have grouped territories we are importing.
                    # So every document is at the smallest unit of territory
                    doc['instanca'] = 4

                    # print '---------'
                    total_votes=0
                    udeo=0
                    for j in range(14, len(row)):
                        doc['rezultat'] = {}
                        doc['rezultat']['glasova'] = int(row[j])
                        if int(row[j]) != 0:
                            total_votes += int(row[j])
                            udeo = (float(int(row[j])) / total_votes) * 100

                        else:
                            udeo = 0.0
                        doc['rezultat']['udeo'] = udeo

                        doc['izbornaLista'] = candidates_or_parties[str(j)]
                        doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                        # print "%s - %s - %s" % (row_count + 1, doc['rezultat']['glasova'], doc['izbornaLista'])
                        docs.append(doc.copy())

                        if len(docs) % 1000 == 0:
                            db[collection].insert(docs)
                            docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)

    def import_data_rest(self, election_type, year, month=None, rnd=None):

        self.prep_import(election_type, year, month, rnd)

        file_path = self.get_data_file_path(election_type, year, month, rnd)

        row_count = 0
        docs = []
        candidates_or_parties = {}
        parent_territory = ''

        with open(file_path, 'rb') as f:
            reader = csv.reader(f)

            for row in tqdm(reader):
                doc = {}

                # Get all the candidates/parties
                if row_count == 0:
                    if int(year) == 2004 and election_type == "predsjednicki":
                        for i in xrange(11, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                    if int(year) == 2008 and election_type == "predsjednicki":
                        for i in xrange(8, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                    if int(year) == 2003 and election_type in ["predsjednicki", "parlamentarni"]:
                        for i in xrange(6, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()
                    elif int(year) == 2002 and election_type == "predsjednicki":
                        for i in xrange(7, len(row)):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()
                    else:
                        for i in xrange(13, len(row), 2):
                            candidates_or_parties[str(i)] = row[i].replace('\n', '').strip()

                elif row_count == 1:
                    pass

                else:

                    if int(year)==2004 and election_type=="predsjednicki":
                        territory = row[1].strip()
                        territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                        polling_station_num = int(row[2].strip())
                        polling_station_address = row[3].strip()
                        ballots_received_count = int(row[4].strip())
                        unused_ballots_count = int(row[5].strip())
                        registered_voters_count = int(row[6].strip())
                        voters_who_voted_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        valid_ballots_count = int(row[10].strip())
                        print row_count

                    else:
                        territory = row[0].strip()
                        territory_slug = slugify(cyrtranslit.to_latin(territory, 'sr'), to_lower=True)
                        polling_station_num = int(row[1].strip()) if row[1].strip() is not '' else row[1].strip()
                        polling_station_address = row[2].strip()
                        registered_voters_count = int(row[3].strip())

                    if int(year) == 2012 and election_type == "predsjednicki":
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        voters_who_voted_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())

                    if int(year) == 2012 and election_type == "parlamentarni":
                        voters_who_voted_count = int(row[4].strip())
                        voters_who_voted_percent = float(row[5].strip())
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        ballots_in_ballot_box_count=int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())


                    if int(year)==2008 and election_type=="predsjednicki":
                        voters_who_voted_count = int(row[6].strip())
                        voters_who_voted_percent=float(row[7].strip())
                    if int(year) not in [2008, 2012]  and election_type != "predsjednicki":
                        voters_who_voted_count = int(row[4].strip())

                    if int(year) == 2003 and election_type in["predsjednicki","parlamentarni"]:
                        total_voter_turn_out = float(row[5].strip())
                    if int(year) == 2002 and election_type == "predsjednicki" and rnd=="prvi":
                        total_voter_turn_out = float(row[4].strip())
                        voters_who_voted_count = int(row[5].strip())
                    if int(year) == 2002 and election_type == "predsjednicki" and rnd=="drugi":
                        voters_who_voted_count = int(row[4].strip())
                        total_voter_turn_out = float(row[5].strip())


                    if int(year) not in [2002, 2003,2004] and election_type not in ["predsjednicki", "parlamentarni"]:
                        voters_who_voted_percent = float(row[5].strip())
                        ballots_received_count = int(row[6].strip())
                        unused_ballots_count = int(row[7].strip())
                        ballots_in_ballot_box_count = int(row[8].strip())
                        invalid_ballots_count = int(row[9].strip())
                        invalid_ballots_percent = float(row[10].strip())
                        valid_ballots_count = int(row[11].strip())
                        valid_ballots_percent = float(row[12].strip())

                    doc['brojUpisanihBiracaUBirackiSpisak'] = registered_voters_count
                    doc['biraciKojiSuGlasali'] = {}
                    if int(year)!=2003 and election_type!="predsjednicki":
                        doc['biraciKojiSuGlasali']['broj'] = voters_who_voted_count

                    if int(year) in [2002, 2003] and election_type in ["predsjednicki", "parlamentarni"]:
                        doc['odzivBiraca']=total_voter_turn_out

                    if int(year) not in [2002, 2003] and election_type not in ["predsjednicki", "parlamentarni"]:
                        doc['biraciKojiSuGlasali']['udeo'] = voters_who_voted_percent
                        doc['brojPrimljenihGlasackihListica'] = ballots_received_count
                        doc['brojNeupoTrebljenihGlasackihListica'] = unused_ballots_count
                        if int(year) not in [2012, 2004] and election_type!="predsjednicki":
                            doc['brojGlasackihListicaUKutiji'] = ballots_in_ballot_box_count
                        doc['brojGlasackihListicaUKutiji'] = {}
                        doc['brojGlasackihListicaUKutiji']['broj'] = invalid_ballots_count
                        if int(year)!=2004 and election_type!="predsjednicki":
                            doc['brojGlasackihListicaUKutiji']['udeo'] = invalid_ballots_percent
                        doc['vazeciGlasackiListici'] = {}
                        doc['vazeciGlasackiListici']['broj'] = valid_ballots_count
                        if int(year) != 2004 and election_type != "predsjednicki":
                            doc['vazeciGlasackiListici']['udeo'] = valid_ballots_percent
                    # Some rows consist of territory grouping.
                    # We need to track those.
                    if cyrtranslit.to_latin(territory, 'sr').isupper():
                        doc['instanca'] = 1

                    elif 'okrug' in territory_slug\
                            or territory_slug in ['grad-beograd', 'inostranstvo']\
                            or territory_slug == 'zavodi-za-izvrsenje-zavodskih-sankcija' and polling_station_num is '':
                        doc['instanca'] = 2
                        parent_territory = territory

                    elif polling_station_num is '':
                        doc['instanca'] = 3
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'), to_lower=True)

                    elif polling_station_num is not '':
                        doc['instanca'] = 4
                        doc['parentTeritorija'] = parent_territory
                        doc['parentTeritorijaSlug'] = slugify(cyrtranslit.to_latin(parent_territory, 'sr'), to_lower=True)
                        doc['brojBirackogMesta'] = polling_station_num
                        doc['adresaBirackogMesta'] = polling_station_address

                    if int(year)==2003 and election_type in ["predsjednicki","parlamentarni"]:
                        total_votes=0
                        udeo=0
                        for j in xrange(6, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}
                            doc['rezultat']['glasova'] = int(row[j])


                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / total_votes) * 100

                            else:
                                udeo = 0.0

                            doc['rezultat']['udeo'] =float(udeo)


                            doc['izbornaLista'] = candidates_or_parties[str(j)]
                            doc['izbornaListaSlug'] = slugify(
                            cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []
                    elif int(year) == 2002 and election_type == "predsjednicki":
                        total_votes=0
                        udeo=0
                        for j in xrange(7, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}


                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / total_votes) * 100
                                print udeo
                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                              to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []
                    elif int(year) == 2004 and election_type == "predsjednicki":
                        total_votes=0
                        udeo=0
                        for j in xrange(11, len(row)):
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}

                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / total_votes) * 100
                                print udeo
                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election

                            month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                            rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                            doc['mesec'] = month_cyr
                            doc['krug'] = rnd_cyr
                            doc['kandidat'] = candidates_or_parties[str(j)].title()
                            doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'),
                                                          to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []

                    else:
                        total_votes=0
                        udeo=0
                        for j in xrange(13, len(row), 2):
                            # Set generic values
                            doc['teritorija'] = territory
                            doc['teritorijaSlug'] = territory_slug
                            doc['izbori'] = cyrtranslit.to_cyrillic(election_type.title(), 'sr')
                            doc['godina'] = int(year)

                            doc['rezultat'] = {}
                            doc['rezultat']['glasova'] = int(row[j])
                            if int(row[j]) != 0:
                                total_votes += int(row[j])
                                udeo = (float(int(row[j])) / total_votes) * 100
                                print udeo
                            else:
                                udeo = 0.0
                            doc['rezultat']['udeo'] = udeo
                            # Set remaining values depending on whether is is a presidential or parliamentary election
                            if election_type == 'predsjednicki':
                                month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                                rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                                doc['mesec'] = month_cyr
                                doc['krug'] = rnd_cyr
                                doc['kandidat'] = candidates_or_parties[str(j)].title()
                                doc['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            else:
                                doc['izbornaLista'] = candidates_or_parties[str(j)]
                                doc['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidates_or_parties[str(j)], 'sr'), to_lower=True)

                            '''
                            if 'parentTerritory' in doc:
                                print '%s - %s - %s - %s' % (row_count+1, doc['instanca'], doc['teritorija'], doc['parentTerritory'])
                            else:
                                print '%s - %s - %s' % (row_count + 1, doc['instanca'], doc['teritorija'])
                            '''

                            docs.append(doc.copy())

                            if len(docs) % 1000 == 0:
                                db[collection].insert(docs)
                                docs = []

                row_count += 1

        # Insert remaining documents
        if len(docs) > 0:
            db[collection].insert(docs)


    def prep_import(self, election_type, year, month=None, rnd=None):
        if election_type == 'predsjednicki':
            print '\nRemoving previously imported data for %s %s %s %s...' % (election_type, year, month, rnd)
            db[collection].remove({
                'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                'godina': int(year),
                'mesec': cyrtranslit.to_cyrillic(month.title(), 'sr'),
                'krug': cyrtranslit.to_cyrillic(rnd.title(), 'sr')
            })

            print 'Importing data for %s %s %s %s...' % (election_type, year, month, rnd)

        else:
            print '\nRemoving previously imported data for %s %s...' % (election_type, year)
            db[collection].remove({
                'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                'godina': int(year)
            })

            print 'Importing data for %s %s...' % (election_type, year)

    def get_data_file_path(self, election_type, year, month=None, rnd=None):
        if election_type == 'predsjednicki':
            return "data/izbori2/%s/%s-%s-%s.csv" % (election_type, year, month, rnd)
        else:
            return "data/izbori2/%s/%s.csv" % (election_type, year)
