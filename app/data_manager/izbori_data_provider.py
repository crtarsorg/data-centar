# coding=utf-8
from app import mongo
import cyrtranslit
from random import randint
from flask import jsonify, request
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
            },

        }


        sort = {
            "rezultat.glasova": -1
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
            'rezultat': 1,

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
            {'$sort': sort},
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
                "kandidat": "$_id.kandidat",
                "glasova": "$glasova",
                "udeo": "$udeo",

            }
        else:
            return {
                "_id": 0,
                'izbornaLista': '$_id.izbornaLista',
                "glasova": "$glasova",
                "udeo": "$udeo",

            }

    def get_top_indicators_by_type(self, data_source,election_type_slug, godina, instanca):
        collection = 'izbori' if data_source == 1 else 'izbori2'

        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': godina,
            'instanca':instanca

        }
        if election_type_slug == 'predsjednicki':
            group = {
                '_id': {
                    'kandidat': '$kandidat'
                },
                'glasova': {"$sum": "$rezultat.glasova"},
                'udeo': {"$sum": "$rezultat.udeo"},


            }
        else:
            group = {
                '_id': {
                    'izbornaLista': '$izbornaLista'
                },
                'glasova': {"$sum": "$rezultat.glasova"},
                'udeo': {"$sum": "$rezultat.udeo"},

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
        print total_votes
        for candidate in rsp['result']:
            print candidate
            candidate["udeo"] = (float(candidate["glasova"]) / total_votes) * 100
        return rsp['result']

    #the function will return data only for parlamentaty elections and for the years 2014, 2016, instanca 4
    def get_total_voters_turnout(self, election_type_slug, godina):
        collection ='izbori2'
        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': godina,

        }
        group = {
            '_id': {
                'teritorija': '$teritorija',

            },
        }
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
            'brojUpisanihBiracaUBirackiSpisak': '$_id.brojUpisanihBiracaUBirackiSpisak',
            'biraciKojiSuGlasali': '$_id.biraciKojiSuGlasali.broj',
        }

        pipeline = [
            {'$match': match},
            {'$group': group},
            {'$project':project}
        ]
        rsp = mongo.db[collection].aggregate(pipeline)
        total_voters=0
        total_registered=0
        percentage=0;
        for rezultat in rsp['result']:
            total_voters+=rezultat['biraciKojiSuGlasali']
            total_registered+=rezultat['brojUpisanihBiracaUBirackiSpisak']
            percentage=(float(total_voters) / total_registered) * 100
        return percentage



    def get_political_parties(self):

        data=[]

        data.append({
            "name":"ЦРНОГОРСКА ПАРТИЈА - ЈОСИП БРОЗ",
            "color":"#AA8E39"
             })
        data.append({
            "name": "ЛИСТА НАЦИОНАЛНИХ ЗАЈЕДНИЦА - ЕМИР ЕЛФИЋ",
            "color": "#2E4372"
        })
        data.append({
            "name": "ДОСТА ЈЕ БИЛО - САША РАДУЛОВИЋ",
            "color": "#29526D"
        })
        data.append({
            "name": "КОАЛИЦИЈА ГРАЂАНА СВИХ НАРОДА И НАРОДНОСТИ",
            "color": "#90305A"
        })
        data.append({
            "name": "ГРУПА ГРАЂАНА ПАТРИОТСКИ ФРОНТ",
            "color": "#A3A838"
        })
        data.append({
            "name": "РУСКА СТРАНКА - СЛОБОДАН НИКОЛИЋ",
            "color": "#6B9A33"
        })
        data.append({
            "name": "ПАРТИЈА ЗА ДЕМОКРАТСКО ДЕЛОВАЊЕ - РИЗА ХАЛИМИ",
            "color": "#412F74"
        })
        data.append({
            "name": "АЛЕКСАНДАР ВУЧИЋ - СНС, СДПС, НС, СПО, ПС",
            "color": "#05a6f0"
        })
        data.append({
            "name": "АЛЕКСАНДАР ВУЧИЋ – БУДУЋНОСТ У КОЈУ ВЕРУЈЕМО (Српска напредна странка Сцијалдемократска партија Србије, Нова Србија, Српски покрет обнове, Покрет социјалиста)",
            "color": "#05a6f0"
        })
        data.append({
            "name": "ИВИЦА ДАЧИЋ - СПС, ПУПС, ЈС",
            "color": "#81bc06"
        })
        data.append({
            "name": "ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - ВОЈИСЛАВ КОШТИНИЦА",
            "color": "#852C62"
        })
        data.append({
            "name":  "ЧЕДОМИР ЈОВАНОВИЋ - ЛДП, БДЗС, СДУ",
            "color": "#852C62"
        })
        data.append({
            "name":  "САВЕЗ ВОЈВОЂАНСКИХ МАЂАРА - ИШТВАН ПАСТОР",
            "color": "#852C62"
        })
        data.append({
            "name":"Српска радикална странка - др Војислав Шешељ",
            "color": "#C80202"
        })
        data.append({
            "name": "УЈЕДИЊЕНИ РЕГИОНИ СРБИЈЕ - МЛАЂАН ДИНКИЋ",
            "color": "#852C62"
        })
        data.append({
            "name":  "СА ДЕМОКРАТСКОМ СТРАНКОМ ЗА ДЕМОКРАТСКУ СРБИЈУ",
            "color": "#852C62"
        })
        data.append({
            "name":"ДВЕРИ - БОШКО ОБРАДОВИЋ",
            "color": "#852C62"
        })
        data.append({
            "name": "СДА САНЏАКА - ДР СУЛЕЈМАН УГЉАНИН",
            "color": "#852C62"
        })
        data.append({
            "name": "БОРИС ТАДИЋ - НДС, ЛСВ, ЗЗС, ВМДК, ЗЗВ, ДЛР",
            "color": "#852C62"
        })
        data.append({
            "name": "ТРЕЋА СРБИЈА - ЗА СВЕ ВРЕДНЕ ЉУДЕ",
            "color": "#852C62"
        })
        data.append({
            "name": "МУАМЕР ЗУКОРЛИЋ / MUAMER ZUKORLIĆ - БОШЊАЧКА ДЕМОКРАТСКА ЗАЈЕДНИЦА САНЏАКА / BOŠNJAČKA DEMOKRATSKA ZAJEDNICA SANDŽAKA",
            "color": "#852C62"
        })
        data.append({
            "name":"SDA Sandžaka – Dr. Sulejman Ugljanin СДА Санџака – Др Сулејман Угљанин",
            "color": "#852C62"
        })
        data.append({
            "name": "За слободну Србију – ЗАВЕТНИЦИ – Милица Ђурђевић",
            "color": "#852C62"
        })
        data.append({
            "name": "Група грађана ЗА ПРЕПОРОД СРБИЈЕ – ПРОФ. ДР СЛОБОДАН КОМАЗЕЦ",
            "color": "#852C62"
        })
        data.append({
            "name":  "Републиканска странка – Republikánus párt – Никола Сандуловић",
            "color": "#852C62"
        })
        data.append({
            "name": "СРПСКО РУСКИ ПОКРЕТ – СЛОБОДАН ДИМИТРИЈЕВИЋ",
            "color": "#852C62"
        })
        data.append({
            "name": "Борко Стефановић – Србија за све нас",
            "color": "#852C62"
        })
        data.append({
            "name": "ДИЈАЛОГ – МЛАДИ СА СТАВОМ – СТАНКО ДЕБЕЉАКОВИЋ",
            "color": "#852C62"
        })
        data.append({
            "name": "ДОСТА ЈЕ БИЛО – САША РАДУЛОВИЋ",
            "color": "#852C62"
        })
        data.append({
            "name":  "ПАРТИЈА ЗА ДЕМОКРАТСКО ДЕЛОВАЊЕ – АРДИТА СИНАНИ PARTIA PËR VEPRIM DEMOKRATIK – ARDITA SINANI",
            "color": "#852C62"
        })
        data.append({
            "name": "ЗЕЛЕНА СТРАНКА",
            "color": "#852C62"
        })
        data.append({
            "name":  "У ИНАТ – СЛОЖНО ЗА СРБИЈУ – НАРОДНИ САВЕЗ",
            "color": "#852C62"
        })
        data.append({
            "name": "АЛЕКСАНДАР ВУЧИЋ - СРБИЈА ПОБЕЂУЈЕ",
            "color": "#05a6f0"
        })
        data.append({
            "name":   "ЗА ПРАВЕДНУ СРБИЈУ - ДЕМОКРАТСКА СТРАНКА (НОВА, ДСХВ, ЗЗС)",
            "color": "#852C62"
        })
        data.append({
            "name": "ИВИЦА ДАЧИЋ -\"Социјалистичка партија Србије (СПС), Јединствена Србија (ЈС) - Драган Марковић Палма\"",
            "color": "#81bc06"
        })
        data.append({
            "name":  "Др ВОЈИСЛАВ ШЕШЕЉ - СРПСКА РАДИКАЛНА СТРАНКА",
            "color": "#852C62"
        })
        data.append({
            "name": "ДВЕРИ - ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - САНДА РАШКОВИЋ ИВИЋ - БОШКО ОБРАДОВИЋ",
            "color": "#852C62"
        })
        data.append({
            "name": "Vajdasági Magyar Szövetség-Pásztor István - Савез војвођанских Мађара-Иштван Пастор",
            "color": "#852C62"
        })
        data.append({
            "name":"БОРИС ТАДИЋ, ЧЕДОМИР ЈОВАНОВИЋ - САВЕЗ ЗА БОЉУ СРБИЈУ - Либерално демократска партија, Лига социјалдемократа Војводине, Социјалдемократска странка",
            "color": "#852C62"
        })
        data.append({
            "name": "Иштван Пастор",
            "color": "#852C62"
        })
        data.append({
            "name":"Маријан Ристичевић",
            "color": "#852C62"
        })
        data.append({
            "name":"Чедомир Јовановић",
            "color": "#852C62"
        })
        data.append({
            "name":"Милутин Мркоњић",
            "color": "#852C62"
        })
        data.append({
            "name": "Томислав Николић",
            "color": "#2A808D"
        })
        data.append({
            "name": "Југослав Добричанин",
            "color": "#852C62"
        })
        data.append({
            "name": "Велимир Илић",
            "color": "#852C62"
        })
        data.append({
            "name":  "Вук Драшковић",
            "color": "#852C62"
        })
        data.append({
            "name": "Велимир-Бата Живојиновић",
            "color": "#852C62"
        })
        data.append({
            "name": "Проф. Др Бранислав-Бане Ивковић",
            "color": "#852C62"
        })

        data.append({
            "name": "Др Мирољуб Лабус",
            "color": "#D4D469"
        })
        data.append({
            "name":"Др Томислав Лалошевић",
            "color": "#852C62"
        })
        data.append({
            "name":   "Др Вук Обрадовић",
            "color": "#852C62"
        })
        data.append({
            "name": "Небојша Павковић",
            "color": "#852C62"
        })
        data.append({
            "name": "Проф. Борислав Пелевић",
            "color": "#852C62"
        })
        data.append({
            "name": "Др Драган Раденовић",
            "color": "#852C62"
        })
        data.append({
            "name":  "Др Војислав Шешељ",
            "color": "#852C62"
        })
        data.append({
            "name": "Војислав Коштуница",
            "color": "#659933"
        })
        data.append({
            "name": "Борислав Пелевић",
            "color": "#852C62"
        })
        data.append({
            "name": "Радослав Авлијаш",
            "color": "#852C62"
        })
        data.append({
            "name": "Проф. Др Драгољуб Мићуновић",
            "color": "#852C62"
        })
        data.append({
            "name":"Марјан Ристичевић",
            "color": "#852C62"
        })
        data.append({
            "name":  "Драган С. Томић",
            "color": "#852C62"
        })
        data.append({
            "name":  "Љиљана Аранђеловић",
            "color": "#852C62"
        })
        data.append({
            "name":   "Владан Батић",
            "color": "#852C62"
        })
        data.append({
            "name": "Ивица Дачић",
            "color": "#852C62"
        })
        data.append({
            "name":  "Милован Дрецун",
            "color": "#852C62"
        })
        data.append({
            "name": "Драган Ђорђевић",
            "color": "#852C62"
        })
        data.append({
            "name": "Проф. Др Бранислав Бане Ивковић",
            "color": "#852C62"
        })
        data.append({
            "name":"Мирко Јовић",
            "color": "#852C62"
        })
        data.append({
            "name":"Јелисавета Карађорђевић",
            "color": "#852C62"
        })
        data.append({
            "name":"Богољуб Карић",
            "color": "#852C62"
        })
        data.append({
            "name":"Драган Маршићанин",
            "color": "#852C62"
        })
        data.append({
            "name":  "Зоран Милинковић",
            "color": "#852C62"
        })
        data.append({
            "name": "Проф. Др Зоран Станковић",
            "color": "#852C62"
        })
        data.append({
            "name": "Владан Глишић",
            "color": "#852C62"
        })
        data.append({
            "name":  "Проф. Др Зоран Драгишић",
            "color": "#852C62"
        })
        data.append({
            "name": "Јадранка Шешељ",
            "color": "#852C62"
        })
        data.append({
            "name": "Муамер Зукорлић",
            "color": "#852C62"
        })
        data.append({
            "name":"Даница Грујичић",
            "color": "#852C62"
        })
        data.append({
            "name": "Борис Тадић",
            "color": "#78BAC2"
        })
        data.append({
            "name": "Демократска странка - Борис Тадић",
            "color": "#141A64"
        })
        data.append({
            "name": "ДЕМОКРАТСКА СТРАНКА СРБИЈЕ-ВОЈИСЛАВ КОШТУНИЦА",
            "color": "#ffffff"
        })
        return data

    def get_winners_for_each_territory(self, data_source,election_type_slug,year,instanca):
        collection = 'izbori' if data_source == 1 else 'izbori2'
        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': year,
            'instanca':instanca
        }
        group = {
            '_id': {
                'teritorija': '$teritorija',
                'teritorijaSlug': '$teritorijaSlug',
            },
            'rezultat': {
                '$push':
                    self.get_push_pipeline_operation_for_votes_grouped_by_territory_group_by_result(
                    election_type_slug)
            },
        }
        project = {
            '_id': 0,
            'teritorija': '$_id.teritorija',
            'teritorijaSlug': '$_id.teritorijaSlug',
            'rezultat': 1,
        }
        pipeline = [
            {'$match': match},

            {'$group': group},
            {'$project': project}
        ]
        rsp = mongo.db[collection].aggregate(pipeline, allowDiskUse=True)
        return rsp['result']





