# coding=utf-8
from app import mongo
import cyrtranslit

class IzboriDataProvider():

    def get_votes_grouped_by_territory(self, election_type_slug, year, territory_slug=None, round_slug=None):

        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': year
        }

        if round_slug is not None:
            round_val = cyrtranslit.to_cyrillic(round_slug.title(), 'sr')
            match['krug'] = round_val
            print round_val

        if territory_slug is not None:
            match['teritorijaSlug'] = territory_slug

        pipeline = [
            {'$match': match},
            {'$group': {
                '_id': {
                    'teritorija': '$teritorija',
                    'teritorijaSlug': '$teritorijaSlug',
                },
                'rezultat': {
                    '$push': self.get_push_pipeline_operation_for_votes_grouped_by_territory_group_by_result(
                        election_type_slug)
                }
            }},
            {'$project': {
                '_id': 0,
                'teritorija': '$_id.teritorija',
                'teritorijaSlug': '$_id.teritorijaSlug',
                'rezultat': 1
            }}
        ]

        rsp = mongo.db['izbori'].aggregate(pipeline)

        if territory_slug is not None:
            return rsp['result'][0]
        else:
            return rsp['result']


    def get_votes_grouped_by_party_or_candidate(self, election_type_slug, year, party_or_candidate_slug=None, round_slug=None):

        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': year
        }

        if round_slug is not None:
            round_val = cyrtranslit.to_cyrillic(round_slug.title(), 'sr')
            match['krug'] = round_val

        if party_or_candidate_slug is not None:
            if election_type_slug == 'predsjednicki':
                match['kandidatSlug'] = party_or_candidate_slug
            else:
                match['izbornaListaSlug'] = party_or_candidate_slug

        pipeline = [
            {'$match': match},
            {'$group': {
                '_id': self.get_id_pipeline_operation_for_votes_grouped_by_party_or_candidate(election_type_slug),
                'rezultat': {
                    '$push': {
                        'teritorija': '$teritorija',
                        'teritorijaSlug': '$teritorijaSlug',
                        'rezultat': '$rezultat'
                    }
                }
            }},
            {'$project': self.get_poject_pipeline_operation_for_votes_grouped_by_party_or_candidate(election_type_slug)}
        ]

        rsp = mongo.db['izbori'].aggregate(pipeline)

        if party_or_candidate_slug is not None:
            return rsp['result'][0]
        else:
            return rsp['result']


    def get_push_pipeline_operation_for_votes_grouped_by_territory_group_by_result(self, election_type_slug):
        if election_type_slug == 'predsjednicki':
            return {
                'kandidat': '$kandidat',
                'kandidatSlug': '$kandidatSlug',
                'rezultat': '$rezultat'
            }
        else:
            return {
                'izbornaLista': '$izbornaLista',
                'izbornaListaSlug': '$izbornaListaSlug',
                'rezultat': '$rezultat'
            }


    def get_id_pipeline_operation_for_votes_grouped_by_party_or_candidate(self, election_type_slug):
        if election_type_slug == 'predsjednicki':
            return {
                'kandidat': '$kandidat',
                'kandidatSlug': '$kandidatSlug',
            }
        else:
            return {
                'izbornaLista': '$izbornaLista',
                'izbornaListaSlug': '$izbornaListaSlug',
            }


    def get_poject_pipeline_operation_for_votes_grouped_by_party_or_candidate(self, election_type_slug):
        if election_type_slug == 'predsjednicki':
            return {
                '_id': 0,
                'kandidat': '$_id.kandidat',
                'kandidatSlug': '$_id.kandidatSlug',
                'rezultat': 1
            }
        else:
            return {
                '_id': 0,
                'izbornaLista': '$_id.izbornaLista',
                'izbornaListaSlug': '$_id.izbornaListaSlug',
                'rezultat': 1
            }