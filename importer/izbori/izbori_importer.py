# coding=utf-8
from flask_pymongo import MongoClient
import xml.etree.ElementTree
import cyrtranslit
from slugify import slugify


# Instantiate mongo client
mongo = MongoClient()

# Create mongo database instance
db = mongo['datacentar']


class IzboriDataImporter(object):

    def import_data(self, election_type, year, month=None, rnd=None):

        self.prep_import(election_type, year, month, rnd)

        file_path = self.get_data_file_path(election_type, year, month, rnd)

        e = xml.etree.ElementTree.parse(file_path).getroot()

        results = {}
        docs = []
        for result in e.findall('Result'):
            territory = result.attrib[u'Територија'].strip()
            data_type = result.attrib[u'Врста_податка'].strip()
            candidate = result.attrib[u'Кандидат'].strip() if election_type == 'predsjednicki' else result.attrib[u'Изборна_листа'].strip()

            # We have two entries per territory. One for share of votes (in percentage) and one for number of votes.
            # We want to save both numbers in the same document
            # To achieve this, we keep track of created documents per territory
            if territory not in results:
                results[territory] = {}

            if candidate not in results[territory]:
                results[territory][candidate] = {
                    'teritorija': territory,
                    'teritorijaSlug': slugify(cyrtranslit.to_latin(territory.encode('utf-8'), 'sr'), to_lower=True),
                    'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                    'godina': int(year),
                    'rezultat': {
                        'udeo': None,
                        'glasova': None
                    }
                }

                if election_type == 'predsjednicki':
                    month_cyr = cyrtranslit.to_cyrillic(month.title(), 'sr')
                    rnd_cyr = cyrtranslit.to_cyrillic(rnd.title(), 'sr')

                    results[territory][candidate]['mesec'] = month_cyr
                    results[territory][candidate]['krug'] = rnd_cyr
                    results[territory][candidate]['kandidat'] = candidate.title()
                    results[territory][candidate]['kandidatSlug'] = slugify(cyrtranslit.to_latin(candidate.encode('utf-8'), 'sr'), to_lower=True)

                else:
                    results[territory][candidate]['izbornaLista'] = candidate
                    results[territory][candidate]['izbornaListaSlug'] = slugify(cyrtranslit.to_latin(candidate.encode('utf-8'), 'sr'), to_lower=True)

            # Удео броја гласова које је добила листа у укупном броју гласова, %
            if '%' in data_type:
                results[territory][candidate]['rezultat']['udeo'] = float(result.text.replace(',', '.'))

            # Број гласова које је добила листа
            else:
                results[territory][candidate]['rezultat']['glasova'] = int(result.text)


            if results[territory][candidate]['rezultat']['udeo'] is not None and results[territory][candidate]['rezultat']['glasova'] is not None:
                docs.append(results[territory][candidate])

        # Insert documents
        db['izbori'].insert(docs)

    def prep_import(self, election_type, year, month=None, rnd=None):
        if election_type == 'predsjednicki':
            print '\nRemoving previously imported data for %s %s %s %s...' % (election_type, year, month, rnd)
            db['izbori'].remove({
                'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                'godina': int(year),
                'mesec': cyrtranslit.to_cyrillic(month.title(), 'sr'),
                'krug': cyrtranslit.to_cyrillic(rnd.title(), 'sr')
            })

            print 'Importing data for %s %s %s %s...' % (election_type, year, month, rnd)

        else:
            print '\nRemoving previously imported data for %s %s...' % (election_type, year)
            db['izbori'].remove({
                'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                'godina': int(year)
            })

            print 'Importing data for %s %s...' % (election_type, year)

    def get_data_file_path(self, election_type, year, month=None, rnd=None):
        if election_type == 'predsjednicki':
            return "data/izbori/%s/%s-%s-%s.xml" % (election_type, year, month, rnd)
        else:
            return "data/izbori/%s/%s.xml" % (election_type, year)