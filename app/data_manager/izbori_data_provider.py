# coding=utf-8
from app import mongo
import cyrtranslit
from random import randint
from flask import jsonify, request
class IzboriDataProvider():

    def get_votes_grouped_by_territory(self, data_source, election_type_slug, year, instanca, territory_slug=None, round_slug=None,range_of_documents=None):
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

        sort = {
            "rezultat.glasova": -1
        }
        group = {
            '_id': {
                'teritorija': '$teritorija',
                'teritorijaSlug': '$teritorijaSlug',
            },
            'rezultat': {
                '$push': self.get_push_pipeline_operation_for_votes_grouped_by_territory_group_by_result(
                    election_type_slug),

            },

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
                {'$project': project},

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
                "izbornaListaSlug": "$_id.izbornaListaSlug",
                'izbornaLista': '$_id.izbornaLista',
                "glasova": "$glasova",
                "udeo": "$udeo",

            }

    def get_top_indicators_by_type(self, data_source,election_type_slug, godina, instanca,round_slug=None):
        collection = 'izbori' if data_source == 1 else 'izbori2'

        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': godina,
            'instanca':instanca

        }

        if election_type_slug == 'predsjednicki':
            if round_slug is not None:
                round_val = cyrtranslit.to_cyrillic(round_slug.title(), 'sr')
                match['krug'] = round_val
            group = {
                '_id': {
                    'kandidat': '$kandidat',
                    'kandidatSlug': '$kandidatSlug'
                },
                'glasova': {"$sum": "$rezultat.glasova"},
                'udeo': {"$sum": "$rezultat.udeo"},

            }
        else:
            group = {
                '_id': {
                    'izbornaLista': '$izbornaLista',
                    'izbornaListaSlug': '$izbornaListaSlug'
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
            {"$match": match},
            {"$group": group_total}
        ]
        rsp_total = mongo.db[collection].aggregate(pipeline_total,allowDiskUse=True)
        rsp = mongo.db[collection].aggregate(pipeline)
        total_votes = rsp_total['result'][0]["total"]

        for candidate in rsp['result']:
            candidate["udeo"] = (float(candidate["glasova"]) / total_votes) * 100
        return rsp['result']

    #the function will return data only for parlamentaty elections and for the years 2014, 2016, instanca 4
    def get_total_voters_turnout(self,data_source, election_type_slug, godina,instanca):
        collection = 'izbori' if data_source == 1 else 'izbori2'
        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': godina,
            'instanca':instanca

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

            if rezultat['brojUpisanihBiracaUBirackiSpisak']!=0:
                total_registered+=rezultat['brojUpisanihBiracaUBirackiSpisak']
            percentage=(float(total_voters) / total_registered) * 100
        return {'percentage':percentage, 'total_voters': total_voters}



    def get_political_parties(self,kandidat_name=None):
        data = []
        #year 2000
        data.append({
            'slug': "demokratska-opozicija-srbije",
            "name": "Демократска опозиција Србије",
            "color": "#AA8E39"
        })
        data.append({
            'slug': "socijalisticka-partija-srbije",
            "name": "Социјалистичка партија Србије",
            "color": "#2E4372"
        })
        data.append({
            'slug': "srpska-radikalna-stranka",
            "name": "Српска радикална странка",
            "color": "#29526D"
        })
        data.append({
            'slug': "stranka-srpskog-jedinstva",
            "name": "Странка Српског јединства",
            "color": "#A3A838"
        })
        data.append({
            'slug': "srpski-pokret-obnove",
            "name": "Српски покрет обнове",
            "color": "#6B9A33"
        })
        data.append({
            'slug': "demokratska-socijalisticka-partija",
            "name": "Демократска социјалистичка партија",
            "color": "#05a6f0"
        })
        data.append({
            'slug': "srpska-socijal-demokratska-partija",
            "name": "Српска социјал-демократска партија",
            "color": "#852C62"
        })
        data.append({
            'slug': "jugoslovenska-levica",
            "name": "Југословенска левица",
            "color": "#81bc06"
        })
        #end of 2000
        data.append({
            'slug':"",
            "name": "ЦРНОГОРСКА ПАРТИЈА - ЈОСИП БРОЗ",
            "color": "#AA8E39"
        })
        data.append({
            'slug': "",
            "name": "ЛИСТА НАЦИОНАЛНИХ ЗАЈЕДНИЦА - ЕМИР ЕЛФИЋ",
            "color": "#2E4372"
        })
        data.append({
            'slug': "",
            "name": "ДОСТА ЈЕ БИЛО - САША РАДУЛОВИЋ",
            "color": "#29526D"
        })

        data.append({
            'slug': "",
            "name": "ГРУПА ГРАЂАНА ПАТРИОТСКИ ФРОНТ",
            "color": "#A3A838"
        })
        data.append({
            'slug': "",
            "name": "РУСКА СТРАНКА - СЛОБОДАН НИКОЛИЋ",
            "color": "#6B9A33"
        })
        data.append({
            'slug': "partija-za-demokratsko-delovanje-riza-halimi",
            "name": "ПАРТИЈА ЗА ДЕМОКРАТСКО ДЕЛОВАЊЕ - РИЗА ХАЛИМИ",
            "color": "#412F74"
        })
        data.append({
            'slug': "aleksandar-vucic-sns-sdps-ns-spo-ps",
            "name": "АЛЕКСАНДАР ВУЧИЋ - СНС, СДПС, НС, СПО, ПС",
            "color": "#05a6f0"
        })
        data.append({
            'slug': "",
            "name": "АЛЕКСАНДАР ВУЧИЋ – БУДУЋНОСТ У КОЈУ ВЕРУЈЕМО (Српска напредна странка Сцијалдемократска партија Србије, Нова Србија, Српски покрет обнове, Покрет социјалиста)",
            "color": "#05a6f0"
        })

        data.append({
            'slug': "",
            "name": "ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - ВОЈИСЛАВ КОШТИНИЦА",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ЧЕДОМИР ЈОВАНОВИЋ - ЛДП, БДЗС, СДУ",
            "color": "#852C62"
        })
        data.append({
            'slug': "savez-vojvodanskih-madara-istvan-pastor",
            "name": "САВЕЗ ВОЈВОЂАНСКИХ МАЂАРА - ИШТВАН ПАСТОР",
            "color": "#852C62"
        })

        data.append({
            'slug': "ujedinjeni-regioni-srbije-mladan-dinkic",
            "name": "УЈЕДИЊЕНИ РЕГИОНИ СРБИЈЕ - МЛАЂАН ДИНКИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "СА ДЕМОКРАТСКОМ СТРАНКОМ ЗА ДЕМОКРАТСКУ СРБИЈУ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ДВЕРИ - БОШКО ОБРАДОВИЋ",
            "color": "#852C62"
        })

        data.append({
            'slug': "",
            "name": "БОРИС ТАДИЋ - НДС, ЛСВ, ЗЗС, ВМДК, ЗЗВ, ДЛР",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ТРЕЋА СРБИЈА - ЗА СВЕ ВРЕДНЕ ЉУДЕ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "МУАМЕР ЗУКОРЛИЋ / MUAMER ZUKORLIĆ - БОШЊАЧКА ДЕМОКРАТСКА ЗАЈЕДНИЦА САНЏАКА / BOŠNJAČKA DEMOKRATSKA ZAJEDNICA SANDŽAKA",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "SDA Sandžaka – Dr. Sulejman Ugljanin СДА Санџака – Др Сулејман Угљанин",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "За слободну Србију – ЗАВЕТНИЦИ – Милица Ђурђевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Група грађана ЗА ПРЕПОРОД СРБИЈЕ – ПРОФ. ДР СЛОБОДАН КОМАЗЕЦ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Републиканска странка – Republikánus párt – Никола Сандуловић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "СРПСКО РУСКИ ПОКРЕТ – СЛОБОДАН ДИМИТРИЈЕВИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Борко Стефановић – Србија за све нас",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ДИЈАЛОГ – МЛАДИ СА СТАВОМ – СТАНКО ДЕБЕЉАКОВИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "dosta-je-bilo-sasa-radulovic",
            "name": "ДОСТА ЈЕ БИЛО – САША РАДУЛОВИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "partija-za-demokratsko-delovanje-ardita-sinani",
            "name": "ПАРТИЈА ЗА ДЕМОКРАТСКО ДЕЛОВАЊЕ – АРДИТА СИНАНИ PARTIA PËR VEPRIM DEMOKRATIK – ARDITA SINANI",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ЗЕЛЕНА СТРАНКА",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "У ИНАТ – СЛОЖНО ЗА СРБИЈУ – НАРОДНИ САВЕЗ",
            "color": "#852C62"
        })
        data.append({
            'slug': "aleksandar-vucic-srbija-pobeduje",
            "name": "АЛЕКСАНДАР ВУЧИЋ - СРБИЈА ПОБЕЂУЈЕ",
            "color": "#05a6f0"
        })
        data.append({
            'slug': "",
            "name": "ЗА ПРАВЕДНУ СРБИЈУ - ДЕМОКРАТСКА СТРАНКА (НОВА, ДСХВ, ЗЗС)",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ИВИЦА ДАЧИЋ -\"Социјалистичка партија Србије (СПС), Јединствена Србија (ЈС) - Драган Марковић Палма\"",
            "color": "#81bc06"
        })
        data.append({
            'slug': "dr-vojislav-seselj-srpska-radikalna-stranka",
            "name": "Др ВОЈИСЛАВ ШЕШЕЉ - СРПСКА РАДИКАЛНА СТРАНКА",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "ДВЕРИ - ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - САНДА РАШКОВИЋ ИВИЋ - БОШКО ОБРАДОВИЋ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Vajdasági Magyar Szövetség-Pásztor István - Савез војвођанских Мађара-Иштван Пастор",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "БОРИС ТАДИЋ, ЧЕДОМИР ЈОВАНОВИЋ - САВЕЗ ЗА БОЉУ СРБИЈУ - Либерално демократска партија, Лига социјалдемократа Војводине, Социјалдемократска странка",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Иштван Пастор",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Маријан Ристичевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Чедомир Јовановић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Милутин Мркоњић",
            "color": "#852C62"
        })
        data.append({
            'slug': "tomislav-nikolic",
            "name": "Томислав Николић",
            "color": "#2A808D"
        })
        data.append({
            'slug': "",
            "name": "Југослав Добричанин",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Велимир Илић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Вук Драшковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Велимир-Бата Живојиновић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Бранислав-Бане Ивковић",
            "color": "#852C62"
        })

        data.append({
            'slug': "",
            "name": "Др Мирољуб Лабус",
            "color": "#D4D469"
        })
        data.append({
            'slug': "",
            "name": "Др Томислав Лалошевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Др Вук Обрадовић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Небојша Павковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Борислав Пелевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Др Драган Раденовић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Др Војислав Шешељ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Војислав Коштуница",
            "color": "#659933"
        })
        data.append({
            'slug': "",
            "name": "Борислав Пелевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Радослав Авлијаш",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Драгољуб Мићуновић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Марјан Ристичевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Драган С. Томић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Љиљана Аранђеловић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Владан Батић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Ивица Дачић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Милован Дрецун",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Драган Ђорђевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Бранислав Бане Ивковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Мирко Јовић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Јелисавета Карађорђевић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Богољуб Карић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Драган Маршићанин",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Зоран Милинковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Зоран Станковић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Владан Глишић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Проф. Др Зоран Драгишић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Јадранка Шешељ",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Муамер Зукорлић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Даница Грујичић",
            "color": "#852C62"
        })
        data.append({
            'slug': "",
            "name": "Борис Тадић",
            "color": "#78BAC2"
        })
        data.append({
            'slug': "",
            "name": "Демократска странка - Борис Тадић",
            "color": "#141A64"
        })
        data.append({
            'slug': "",
            "name": "ДЕМОКРАТСКА СТРАНКА СРБИЈЕ-ВОЈИСЛАВ КОШТУНИЦА",
            "color": "#ffffff"
        })
        data.append({
            'slug': "za-evropsku-srbiju-boris-tadic",
            "name": "ЗА ЕВРОПСКУ СРБИЈУ - БОРИС ТАДИЋ",
            "color": "#141A64"
        })
        data.append({
            'slug': "srpska-radikalna-stranka-dr-vojislav-seselj",
            "name": "Српска радикална странка - др Војислав Шешељ",
            "color": "#90CAF9"
        })
        data.append({
            'slug': "srs",
            "name": "СРС",
            "color": "#003B20"
        })
        data.append({
            'slug': "dss",
            "name": "ДСС",
            "color": "#141A64"
        })
        data.append({
            'slug': "sda-sandzaka-dr-sulejman-ugljanin",
            "name": "СДА САНЏАКА - ДР СУЛЕЈМАН УГЉАНИН",
            "color": "green"
        })
        data.append({
            'slug': "ds",
            "name": "ДС",
            "color": "#141A64"
        })
        data.append({
            'slug': "spo-ns",
            "name": "СПО - НС",
            "color": "#141A69"
        })
        data.append({
            'slug': "da",
            "name": "ДА",
            "color": "#313975"
        })
        data.append({
            'slug': "sps",
            "name": "СПС",
            "color": "#297B48"
        })
        data.append({
            'slug': "g17-plus",
            "name": "Г17 плус",
            "color": "#AAA939"
        })
        data.append({
            'slug': "zajedno-za-toleranciju",
            "name": "Заједно за толеранцију",
            "color": "#AA9239"
        })
        data.append({
            'slug': "za-narodno-jedinstvo",
            "name": "За народно јединство",
            "color": "#00A75B"
        })
        data.append({
            'slug': "otpor",
            "name": "Отпор",
            "color": "#FFC841"
        })
        data.append({
            'slug': "",
            "name": "Демократска странка Србије - Нова Србија - Војислав Коштуница",
            "color": "#2D4571"
        })
        data.append({
            'slug': "",
            "name": "БОШЊАЧКА ЛИСТА ЗА ЕВРОПСКИ САНЏАК - ДР СУЛЕЈМАН УГЉАНИН",
            "color": "#2D882D"
        })
        data.append({
            'slug': "samostalna-srbija",
            "name": "Самостална Србија",
            "color": "#ACD270"
        })
        data.append({
            'slug': "sns",
            "name": "СНС",
            "color": "#27784D"
        })
        data.append({
            'slug': "liberali-srbije",
            "name": "Либерали Србије",
            "color": "#27784D"
        })
        data.append({
            'slug':'pokrenimo-srbiju-tomislav-nikolic',
            "name": "Покренимо Србију - Томислав Николић",
            "color": "#27784D"
        })
        data.append({
            'slug': 'odbrana-i-pravda',
            "name": "Одбрана и правда",
            "color": "#141A64"
        })
        data.append({
            'slug': 'privredna-snaga-srbije-i-dijaspora',
            "name": "Привредна снага Србије и дијаспора",
            "color": "#6E8999"
        })
        data.append({
            'slug': 'reformisti',
            "name": "Реформисти",
            "color": "#CA4400"
        })
        data.append({
            'slug': "izbor-za-bolji-zivot-boris-tadic",
            "name": "Избор за бољи живот - Борис Тадић",
            "color": "#6E8999"
        })
        data.append({
            'slug': "laburist-partija-srbije",
            "name": "Лабурист. партија Србије",
            "color": "#2D4571"
        })
        data.append({
            'slug': "jul",
            "name": " ЈУЛ",
            "color": "#ACD270"
        })
        data.append({
            'slug': "savez-srba-vojvodine",
            "name": " Савез Срба Војводине",
            "color": "#4C691D"
        })
        data.append({
            'slug': "pokret-radnika-i-seljaka",
            "name": "Покрет радника и сељака",
            "color": "#76746F"
        })
        data.append({
            'slug': "komunisticka-partija-josip-broz",
            "name": "Комунистичка партија - Јосип Броз",
            "color": "#C7B588"
        })
        data.append({
            'slug': "ivica-dacic-socijalisticka-partija-srbije-sps-partija-ujedinjenih-penzionera-srbije-pups-jedinstvena-srbija-js",
            "name": 'Ивица Дачић - "Социјалистичка партија Србије (СПС), Партија уједињених пензионера Србије (ПУПС), Јединствена Србија (ЈС)"',
            "color": "#06320C"
        })
        data.append({
            'slug': "savez-vojodanskih-madara-istvan-pastor",
            "name": 'Савез војођанских Мађара - Иштван Пастор',
            "color": "#009D13"
        })
        data.append({
            'slug': "stranka-demokratske-akcije-sandzaka-dr-sulejman-ugljanin",
            "name": 'Странка демократске акције Санџака - др Сулејман Угљанин',
            "color": "#FFC841"
        })
        data.append({
            'slug': "demokratska-stranka-srbije-vojislav-kostunica",
            "name": 'Демократска странка Србије - Војислав Коштуница',
            "color": "#CA4400"
        })
        data.append({
            'slug': "koalicija-albanaca-presevske-doline",
            "name": 'Коалиција Албанаца Прешевске долине',
            "color": "#00A75B"
        })
        data.append({
            'slug': "reformisticka-stranka-prof-dr-milan-visnjic",
            "name": 'Реформистичка странка - проф. др Милан Вишњић',
            "color": "#7EC1A3"
        })
        data.append({
            'slug': "crnogorska-partija-nenad-stevovic",
            "name": 'Црногорска партија - Ненад Стевовић',
            "color": "#003B20"
        })
        data.append({
            'slug': "socijaldemokratski-savez-nebojsa-lekovic",
            "name": 'Социјалдемократски савез - Небојша Лековић',
            "color": "#310CA6"
        })
        data.append({
            'slug': "sve-zajedno-bdz-gsm-dzh-dzvm-slovacka-stranka-emir-elfic",
            "name": 'Све заједно: БДЗ, ГСМ, ДЗХ, ДЗВМ, Словачка странка - Емир Елфић',
            "color": "#ACD270"
        })
        data.append({
            'slug': "nijedan-od-ponudenih-odgovora",
            "name": 'Ниједан од понуђених одговора',
            "color": "#4C691D"
        })
        data.append({
            'slug': "cedomir-jovanovic-preokret",
            "name": 'Чедомир Јовановић - Преокрет',
            "color": "#AC873D"
        })
        data.append({
            'slug': "dveri-za-zivot-srbije",
            "name": 'Двери за живот Србије',
            "color": "#4F4633"
        })
        data.append({
            'slug': "dveri-za-zivot-srbije",
            "name": 'Двери за живот Србије',
            "color": "#4F4633"
        })
        data.append({
            'slug': "ivica-dacic-sps-js-dragan-markovic-palma",
            "name": 'ИВИЦА ДАЧИЋ - СПС, ЈС - Драган Марковић Палма',
            "color": "#4F4633"
        })
        #presidential canditates
        data.append({
            'slug': "demokratska-stranka-srbije-nova-srbija-dr-vojislav-kostunica",
            "name": 'Демократска странка Србије - Нова Србија - др Војислав Коштуница',
            "color": "#4F4633"
        })
        data.append({
            'slug': "vojislav-kostunica-dss",
            "name": 'Војислав Коштуница (ДСС)',
            "color": "#AC873D"
        })
        data.append({
            'slug': "dr-miroljub-labus-gg",
            "name": 'др Мирољуб Лабус (ГГ)',
            "color": "#AC873D"
        })
        data.append({
            'slug': "tomislav-nikolic",
            "name": 'Tomislav Nikolić',
            "color": "#AC873D"
        })
        data.append({
            'slug': "borislav-pelevic-ssj",
            "name": 'Борислав Пелевић (ССЈ)',
            "color": "#009D13"
        })

        data.append({
            'slug': "demokratska-stranka-srbije-vojislav-kostinica",
            "name": 'ДЕМОКРАТСКА СТРАНКА СРБИЈЕ - ВОЈИСЛАВ КОШТИНИЦА',
            "color": "#009D13"
        })
        data.append({
            'slug': "ivica-dacic-sps-pups-js",
            "name": 'ИВИЦА ДАЧИЋ - СПС, ПУПС, ЈС',
            "color": "blue"
        })


        if kandidat_name is not None:
            jsondata={}
            selected_color=""
            for name in data:
                if kandidat_name==name['slug']:
                    jsondata={'color':name['color'],'slug':name['slug'],'name':name['name']}

            return jsondata
        else:
            print "not none"
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
                'brojUpisanihBiracaUBirackiSpisak':'$brojUpisanihBiracaUBirackiSpisak',
                'biraciKojiSuGlasali':'$biraciKojiSuGlasali.broj'

            },
            'rezultat': {
                '$push':
                    self.get_push_pipeline_operation_for_votes_grouped_by_territory_group_by_result(
                    election_type_slug)
            },
        }
        sort = {
            "rezultat.glasova": -1
        }
        project = {
            '_id': 0,
            'teritorija': '$_id.teritorija',
            'teritorijaSlug': '$_id.teritorijaSlug',
            'brojUpisanihBiracaUBirackiSpisak': "$_id.brojUpisanihBiracaUBirackiSpisak",
            'biraciKojiSuGlasali': "$_id.biraciKojiSuGlasali",
            "percentage": {"$multiply": [{"$divide": [100, '$_id.brojUpisanihBiracaUBirackiSpisak']}, "$_id.biraciKojiSuGlasali"]},
            'rezultat': 1,
        }


        pipeline = [
            {'$match': match},
            {'$sort': sort},
            {'$group': group},
            {'$project': project}
        ]
        rsp = mongo.db[collection].aggregate(pipeline, allowDiskUse=True)


        return rsp['result']

    def get_results_by_territory(self, data_source, election_type_slug, year,territory_slug,instanca):
        collection = 'izbori' if data_source == 1 else 'izbori2'

        match = {
            'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
            'godina': year,
            'teritorijaSlug':territory_slug,
            'instanca':instanca

        }

        # For now, we only support territorial levels for parliament elections
        group = {
            '_id': {
                'teritorija': '$teritorija',
                'teritorijaSlug': '$teritorijaSlug',
            },
            'rezultat': {
                '$push': self.get_push_pipeline_operation_for_votes_grouped_by_territory_group_by_result(
                    election_type_slug),

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

        return rsp['result'][0]


    def get_results_by_territory_by_candidate(self,data_source,election_type_slug,year,territory_slug,candidate_slug,instanca):
        collection = 'izbori' if data_source == 1 else 'izbori2'
        if election_type_slug == 'predsjednicki':
            match = {
                'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
                'godina': year,
                'teritorijaSlug': territory_slug,
                'instanca': instanca,
                'kandidatSlug':candidate_slug
            }
            group = {
                '_id': {
                    'teritorija': '$teritorija',
                    'teritorijaSlug': '$teritorijaSlug',
                    'teritorija': '$teritorija',
                    'izbornaLista': '$izbornaLista',
                    'izbornaListaSlug': '$izbornaListaSlug',
                },
            }
        else:
            match = {
                'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
                'godina': year,
                'teritorijaSlug': territory_slug,
                'instanca': instanca,
                'izbornaListaSlug': candidate_slug
            }
            match1= {
                'izbori': cyrtranslit.to_cyrillic(election_type_slug.title(), 'sr'),
                'godina': year,
                'teritorijaSlug': territory_slug,
                'instanca': instanca,

            }
            group = {
                '_id': {
                    'teritorija': '$teritorija',
                    'teritorijaSlug': '$teritorijaSlug',
                    'teritorija': '$teritorija',
                    'izbornaLista': '$izbornaLista',
                    'izbornaListaSlug': '$izbornaListaSlug',
                    'brojUpisanihBiracaUBirackiSpisak': '$brojUpisanihBiracaUBirackiSpisak',
                    'biraciKojiSuGlasali': '$biraciKojiSuGlasali',
                    'rezultat': '$rezultat'
                },
            }

        project = {
                '_id': 0,
                'teritorija': '$_id.teritorija',
                'teritorijaSlug': '$_id.teritorijaSlug',
                'izbornaListaSlug':'$_id.izbornaListaSlug',
                'izbornaLista': '$_id.izbornaLista',
                'brojUpisanihBiracaUBirackiSpisak':'$_id.brojUpisanihBiracaUBirackiSpisak',
                'biraciKojiSuGlasali':'$_id.biraciKojiSuGlasali',
                'rezultat': '$_id.rezultat',

            }
        pipeline = [
            {'$match': match},
            {'$group':group},
            {'$project': project}
        ]
        sort = {
            "rezultat.glasova": 1
        }
        pipeline1 = [
            {'$match': match1},
            {'$sort':sort},
            {'$group': group},
            {'$project': project}
        ]

        rsp = mongo.db[collection].aggregate(pipeline)
        rsp1 = mongo.db[collection].aggregate(pipeline1)
        return {'array1':rsp['result'][0],'array2':rsp1['result']}









