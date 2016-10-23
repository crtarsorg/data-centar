# coding=utf-8
from app import mongo
import cyrtranslit

class IzboriDataProvider():

    def get_votes_grouped_by_territory(self, election_type_slug, year, territory_slug=None):

        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': year
        }

        # TODO: Convert latin input to cyrillic
        if territory_slug is not None:
            match['teritorijaSlug'] = territory_slug

        rsp = mongo.db['izbori'].aggregate([
            {'$match': match},
            {'$group': {
                '_id': {
                    'teritorija': '$teritorija',
                    'teritorijaSlug': '$teritorijaSlug',
                },
                'rezultat': {
                    '$push': {
                        'izbornaLista': '$izbornaLista',
                        'izbornaListaSlug': '$izbornaListaSlug',
                        'rezultat': '$rezultat'
                    }
                }
            }},
            {'$project': {
                '_id': 0,
                'teritorija': '$_id.teritorija',
                'teritorijaSlug': '$_id.teritorijaSlug',
                'rezultat': 1
            }}
        ])

        if territory_slug is not None:
            return rsp['result'][0]
        else:
            return rsp['result']


    def get_votes_grouped_by_party(self, election_type_slug, year, izborna_lista_slug=None):

        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': year
        }

        # TODO: Convert latin input to cyrillic
        if izborna_lista_slug is not None:
            match['izbornaListaSlug'] = izborna_lista_slug

        rsp = mongo.db['izbori'].aggregate([
            {'$match': match},
            {'$group': {
                '_id': {
                    'izbornaLista': '$izbornaLista',
                    'izbornaListaSlug': '$izbornaListaSlug',
                },
                'rezultat': {
                    '$push': {
                        'teritorija': '$teritorija',
                        'teritorijaSlug': '$teritorijaSlug',
                        'rezultat': '$rezultat'
                    }
                }
            }},
            {'$project': {
                '_id': 0,
                'izbornaLista': '$_id.izbornaLista',
                'izbornaListaSlug': '$_id.izbornaListaSlug',
                'rezultat': 1
            }}
        ])

        if izborna_lista_slug is not None:
            return rsp['result'][0]
        else:
            return rsp['result']