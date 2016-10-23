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

    def import_data(self, election_type, year):

        print '\nRemoving previously imported data for %s %s...' % (election_type, year)
        db['izbori'].remove({
            'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
            'godina': int(year)
        })

        print 'Importing data for %s %s...' % (election_type, year)

        file_path = "data/izbori/" + election_type + "/" + year + ".xml"
        e = xml.etree.ElementTree.parse(file_path).getroot()

        results = {}
        docs = []
        for result in e.findall('Result'):
            territory = result.attrib[u'Територија'].strip()
            data_type = result.attrib[u'Врста_податка'].strip()
            party = result.attrib[u'Изборна_листа'].strip()

            # We have two entries per territory. One for share of votes (in percentage) and one for number of votes.
            # We want to save both numbers in the same document
            # To achieve this, we keep track of created documents per territory
            if territory not in results:
                results[territory] = {}

            if party not in results[territory]:
                results[territory][party] = {
                    'teritorija': territory,
                    'teritorijaSlug': slugify(cyrtranslit.to_latin(territory.encode('utf-8'), 'sr'), to_lower=True),
                    'izbornaLista': party,
                    'izbornaListaSlug': slugify(cyrtranslit.to_latin(party.encode('utf-8'), 'sr'), to_lower=True),
                    'izbori': cyrtranslit.to_cyrillic(election_type.title(), 'sr'),
                    'godina': int(year),
                    'rezultat': {
                        'udeo': None,
                        'glasova': None
                    }
                }

            # Удео броја гласова које је добила листа у укупном броју гласова, %
            if '%' in data_type:
                results[territory][party]['rezultat']['udeo'] = float(result.text.replace(',', '.'))

            # Број гласова које је добила листа
            else:
                results[territory][party]['rezultat']['glasova'] = int(result.text)


            if results[territory][party]['rezultat']['udeo'] is not None and results[territory][party]['rezultat']['glasova'] is not None:
                docs.append(results[territory][party])

        # Insert documents
        db['izbori'].insert(docs)

