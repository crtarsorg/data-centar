# coding=utf-8
from app import mongo
import cyrtranslit

class IzboriDataProvider():

    def get_votes_grouped_by_territory(self, data_source, election_type_slug, year, instanca=None, territory_slug=None, round_slug=None):
        collection = 'izbori' if data_source == 1 else 'izbori2'

        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': year
        }

        # For now, we only support territorial levels for parliament elections
        if election_type_slug != 'predsjednicki' and instanca is not None:
            match['instanca'] = instanca

        if round_slug is not None:
            round_val = cyrtranslit.to_cyrillic(round_slug.title(), 'sr')
            match['krug'] = round_val

        if territory_slug is not None:
            match['teritorijaSlug'] = territory_slug

        group = {
            '_id': {
                'teritorija': '$teritorija',
                'teritorijaSlug': '$teritorijaSlug',
            },
            'rezultat': {
                '$push': self.get_push_pipeline_operation_for_votes_grouped_by_territory_group_by_result(
                    election_type_slug)
            }
        }

        if data_source == 2:
            group['_id']['parentTeritorija'] = '$parentTeritorija'
            group['_id']['parentTeritorijaSlug'] = '$parentTeritorijaSlug'
            group['_id']['adresaBirackogMesta'] = '$adresaBirackogMesta'
            group['_id']['koordinateBirackomMestu'] = '$koordinateBirackomMestu'
            group['_id']['brojUpisanihBiracaUBirackiSpisak'] = '$brojUpisanihBiracaUBirackiSpisak'
            group['_id']['biraciKojiSuGlasali'] = '$biraciKojiSuGlasali'
            group['_id']['brojPrimljenihGlasackihListica'] = '$brojPrimljenihGlasackihListica'
            group['_id']['brojNeupoTrebljenihGlasackihListica'] = '$brojNeupoTrebljenihGlasackihListica'
            group['_id']['brojGlasackihListicaUKutiji'] = '$brojGlasackihListicaUKutiji'
            group['_id']['vazeciGlasackiListici'] = '$vazeciGlasackiListici'

        project = {
            '_id': 0,
            'teritorija': '$_id.teritorija',
            'teritorijaSlug': '$_id.teritorijaSlug',
            'rezultat': 1
        }

        if data_source == 2:
            project['parentTeritorija'] = '$_id.parentTeritorija'
            project['parentTeritorijaSlug'] = '$_id.parentTeritorijaSlug'
            project['adresaBirackogMesta'] = '$_id.adresaBirackogMesta'
            project['koordinateBirackomMestu'] = '$_id.koordinateBirackomMestu'
            project['brojUpisanihBiracaUBirackiSpisak'] = '$_id.brojUpisanihBiracaUBirackiSpisak'
            project['biraciKojiSuGlasali'] = '$_id.biraciKojiSuGlasali'
            project['brojPrimljenihGlasackihListica'] = '$_id.brojPrimljenihGlasackihListica'
            project['brojNeupoTrebljenihGlasackihListica'] = '$_id.brojNeupoTrebljenihGlasackihListica'
            project['brojGlasackihListicaUKutiji'] = '$_id.brojGlasackihListicaUKutiji'
            project['vazeciGlasackiListici'] = '$_id.vazeciGlasackiListici'

        pipeline = [
            {'$match': match},
            {'$group': group},
            {'$project': project}
        ]

        rsp = mongo.db[collection].aggregate(pipeline, allowDiskUse=True)

        return rsp['result']

    def get_votes_grouped_by_party_or_candidate(self, data_source, election_type_slug, year, party_or_candidate_slug=None, round_slug=None):
        collection = 'izbori' if data_source == 1 else 'izbori2'

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

        group = {
            '_id': self.get_id_pipeline_operation_for_votes_grouped_by_party_or_candidate(election_type_slug),
            'rezultat': {
                '$push': {
                    'teritorija': '$teritorija',
                    'teritorijaSlug': '$teritorijaSlug',
                    'rezultat': '$rezultat'
                }
            }
        }

        if data_source == 2:
            group['_id']['parentTeritorija'] = '$parentTeritorija'
            group['_id']['parentTeritorijaSlug'] = '$parentTeritorijaSlug'
            group['_id']['adresaBirackogMesta'] = '$adresaBirackogMesta'
            group['_id']['koordinateBirackomMestu'] = '$koordinateBirackomMestu'
            group['_id']['brojUpisanihBiracaUBirackiSpisak'] = '$brojUpisanihBiracaUBirackiSpisak'
            group['_id']['biraciKojiSuGlasali'] = '$biraciKojiSuGlasali'
            group['_id']['brojPrimljenihGlasackihListica'] = '$brojPrimljenihGlasackihListica'
            group['_id']['brojNeupoTrebljenihGlasackihListica'] = '$brojNeupoTrebljenihGlasackihListica'
            group['_id']['brojGlasackihListicaUKutiji'] = '$brojGlasackihListicaUKutiji'
            group['_id']['vazeciGlasackiListici'] = '$vazeciGlasackiListici'

        pipeline = [
            {'$match': match},
            {'$group': group},
            {'$project': self.get_poject_pipeline_operation_for_votes_grouped_by_party_or_candidate(election_type_slug)}
        ]

        rsp = mongo.db[collection].aggregate(pipeline)

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

    def get_push_pipeline_operation_for_top_indicators(self, election_type_slug):

        if election_type_slug == 'predsjednicki':
            return {
                "_id": 0,
                "kandidatSlug": "$_id.kandidatSlug",
                "glasova": "$glasova",
                "udeo": "$udeo",
            }
        else:
            return {
                "_id": 0,
                'izbornaLista': '$izbornaLista',
                'izbornaListaSlug': '$izbornaListaSlug',
                "glasova": "$glasova",
                "udeo": "$udeo",
            }

    def get_top_indicators_by_type(self, election_type_slug, godina, round_slug=None):

        collection = 'izbori'
        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': godina

        }

        if round_slug is not None:
            round_val = cyrtranslit.to_cyrillic(round_slug.title(), 'sr')
            match['krug'] = round_val

        if election_type_slug == 'predsjednicki':
            group = {
                '_id': {
                    'kandidatSlug': '$kandidatSlug'
                },
                'glasova': {"$sum": "$rezultat.glasova"},
                'udeo': {"$sum": "$rezultat.udeo"}
            }
        else:
            group = {
                '_id': {
                    'kandidatSlug': '$kandidatSlug'
                },
                'glasova': {"$sum": "$rezultat.glasova"},
                'udeo': {"$sum": "$rezultat.udeo"}
            }

        group_total = {
            "_id": None,
            "total": {
                "$sum": "$rezultat.glasova"
            }
        }
        sort = {
            "glasova": -1
        }
        pipeline = [
            {'$match': match},
            {'$group': group},
            {'$sort': sort},
            {'$project': self.get_push_pipeline_operation_for_top_indicators(election_type_slug)}
        ]
        pipeline_total = [
            {"$match": match},
            {"$group": group_total}
        ]
        rsp_total = mongo.db[collection].aggregate(pipeline_total)
        rsp = mongo.db[collection].aggregate(pipeline)
        total_votes = rsp_total['result'][0]["total"]

        for candidate in rsp['result']:
            print candidate
            candidate["udeo"] = (float(candidate["glasova"]) / total_votes) * 100
        return [rsp['result'][0], rsp['result'][1]]
