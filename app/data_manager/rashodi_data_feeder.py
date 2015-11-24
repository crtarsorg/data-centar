# coding=utf-8
from app import mongo
import re
from bson.regex import Regex


class RashodiDataFeed():

    def calculate_sum_of_expenditure_types(self, query_params):

        # Build match pipeline
        match = {
            "$match": {
                "tipPodataka.slug": "rashodi",
            }
        }

        if "filteri" in query_params:

            ### Let's set the values rage for ukupno ###
            if "ukupno" in query_params["filteri"]:
                match['$match']["ukupno"] = {
                    "$gte": int(query_params["filteri"]["ukupno"]["veceIliJednako"]),
                    "$lte": int(query_params["filteri"]["ukupno"]["manjeIliJednako"])
                }

            ### Let's set the values rage for sopstveniPrihodi ###
            if "sopstveniPrihodi" in query_params["filteri"]:
                match['$match']["sopstveniPrihodi"] = {
                    "$gte": query_params["filteri"]["sopstveniPrihodi"]["veceIliJednako"],
                    "$lte": query_params["filteri"]["sopstveniPrihodi"]["manjeIliJednako"]
                }

            ### Let's set the values rage for prihodiBudzeta ###
            if "prihodiBudzeta" in query_params["filteri"]:
                match['$match']["prihodiBudzeta"] = {
                    "$gte": query_params["filteri"]["prihodiBudzeta"]["veceIliJednako"],
                    "$lte": query_params["filteri"]["prihodiBudzeta"]["manjeIliJednako"]
                }

            ### Let's set the values rage for donacije ###
            if "donacije" in query_params["filteri"]:
                match['$match']["donacije"] = {
                    "$gte": query_params["filteri"]["donacije"]["veceIliJednako"],
                    "$lte": query_params["filteri"]["donacije"]["manjeIliJednako"]
                }

            ### Let's set the values rage for ostali ###
            if "ostali" in query_params["filteri"]:
                match['$match']["ostali"] = {
                    "$gte": query_params["filteri"]["ostali"]["veceIliJednako"],
                    "$lte": query_params["filteri"]["ostali"]["manjeIliJednako"]
                }

        # Add other filters
        if query_params['godine'] != []:
            match['$match']["godina"] = {'$in': query_params['godine']}

        if query_params['opstine'] != []:
            match['$match']["opstina.slug"] = {'$in': query_params['opstine']}

        # Build group pipeline
        group = {
            "$group": {
                "_id": {
                    "opstina": "$opstina.latinica",
                    "godina": "$godina",
                    "tipPodataka": "$tipPodataka.vrednost"
                },
                "prihodiBudzeta": {"$sum": "$prihodiBudzeta"},
                "sopstveniPrihodi": {"$sum": "$sopstveniPrihodi"},
                "donacije": {"$sum": "$donacije"},
                "ostali": {"$sum": "$ostali"},
                "ukupno": {"$sum": "$ukupno"}
            }
        }

        # Build project pipeline
        project = {
            "$project": {
                "_id": 0,
                "opstina": "$_id.opstina",
                "godina": "$_id.godina",
                "tipPodataka": "$_id.tipPodataka",
                "prihodiBudzeta": "$prihodiBudzeta",
                "sopstveniPrihodi": "$sopstveniPrihodi",
                "donacije": "$donacije",
                "ostali": "$ostali",
                "ukupno": "$ukupno",
            }
        }

        if "klasifikacija" in query_params:

            if query_params['klasifikacija']['broj'] != []:

                if 'pocinjeSa' in query_params['klasifikacija']:

                    # Let's filter based on class options we picked and regex class number
                    match['$match']['$or'] = []
                    match_class_number = {"klasifikacija.broj": {'$in': query_params['klasifikacija']['broj']}}
                    match['$match']['$or'].append(match_class_number)


                    # Since Pymongo driver works with python regex logic, our pattern should be adopted in a way that python
                    # regex compiler understands, then convert it to a BSON Regex instance,
                    # read more: http://api.mongodb.org/python/current/api/bson/regex.html
                    pattern = re.compile("^%s" % query_params['klasifikacija']['pocinjeSa'])
                    regex = Regex.from_native(pattern)
                    regex.flags ^= re.UNICODE

                    # Build match pipeline
                    match_regex =  {
                        "klasifikacija.broj": regex
                    }

                    match['$match']['$or'].append(match_regex)
                else:
                    match['$match']["klasifikacija.broj"] = {'$in': query_params['klasifikacija']['broj']}

            else:
                pattern = re.compile("^%s" % query_params['klasifikacija']['pocinjeSa'])
                regex = Regex.from_native(pattern)
                regex.flags ^= re.UNICODE
                # Build match pipeline
                match['$match']["klasifikacija.broj"] = regex

            # Add this to param to group and project stages
            group['$group']['_id']['klasifikacijaBroj'] = "$klasifikacija.broj"
            project['$project']['klasifikacijaBroj'] = '$_id.klasifikacijaBroj'


        elif "kategorijaRoditelj" in query_params:
            if query_params['kategorijaRoditelj'] != []:
                match['$match']["kategorijaRoditelj.broj"] = {'$in': query_params['kategorijaRoditelj']}
            group['$group']['_id']['kategorijaRoditelj'] = "$kategorijaRoditelj.broj"
            project['$project']['kategorijaRoditelj'] = '$_id.kategorijaRoditelj'

        # Execute mongo request
        json_doc = mongo.db.opstine.aggregate([match, group, project])

        return json_doc['result']


    def build_json_response_for_parent_categories(self, query_params):

        # Build match pipeline
        match = {
            "$match": {
                "tipPodataka.slug": query_params['tipPodataka']
            }
        }

        if query_params['godine'] != []:
            match['$match']["godina"] = {'$in': query_params['godine']}

        if query_params['opstine'] != []:
            match['$match']["opstina.slug"] = {'$in': query_params['opstine']}

        # Build group pipeline
        group = {
            "$group": {
                "_id": {
                    "broj": "$kategorijaRoditelj.broj",
                    "opis": "$kategorijaRoditelj.opis",
                },
                "klasifikacijaBroj": { "$push":  { "broj": "$klasifikacija.broj", "opis": "$klasifikacija.opis" } }
            }
        }

        # Build project pipeline
        project = {
            "$project": {
                "_id": 0,
                "broj": "$_id.broj",
                "opis": "$_id.opis",
                "klasifikacijaBroj": "$klasifikacijaBroj"
            }
        }
        # Execute mongo request
        json_doc = mongo.db.opstine.aggregate([match, group, project])

        return json_doc['result']


    def retrieve_aggregated_classification_info_for_municipalities(self, query_params):


        match = {
            "$match": {
                "tipPodataka.slug": "rashodi"
            }
        }

        if query_params['godine'] != []:
            match['$match']["godina"] = {'$in': query_params['godine']}

        if query_params['klasifikacijaBroj'] != []:
            query_params['klasifikacijaBroj'] = [str(i) for i in query_params['klasifikacijaBroj']]
            match['$match']["klasifikacija.broj"] = {'$in': query_params['klasifikacijaBroj']}

        # Build group pipeline
        group = {
            "$group": {
                "_id": {
                    "opstina": "$opstina.latinica",
                    "godina": "$godina",
                    "broj": "$klasifikacija.broj",
                    "opis": "$klasifikacija.opis.latinica",
                },
                "prihodiBudzeta": {"$sum": "$prihodiBudzeta"},
                "sopstveniPrihodi": {"$sum": "$sopstveniPrihodi"},
                "donacije": {"$sum": "$donacije"},
                "ostali": {"$sum": "$ostali"},
                "ukupno": {"$sum": "$ukupno"}
            }
        }
        # gather all classifications info to the respective municipality json
        group2 = {
            "$group": {
                "_id": "$_id.opstina",
                "klasifikacije": {
                    "$push": {
                        "godina": "$_id.godina",
                        "broj": "$_id.broj",
                        "opis": "$_id.opis",
                        "prihodiBudzeta":"$prihodiBudzeta",
                        "sopstveniPrihodi": "$sopstveniPrihodi",
                        "donacije": "$donacije",
                        "ostali": "$ostali",
                        "ukupno": "$ukupno"

                    }
                }
            }
        }

        # Build project pipeline
        project = {
            "$project": {
                "_id": 0,
                "opstina": "$_id",
                "klasifikacije": "$klasifikacije"

            }
        }

        # Execute mongo request
        json_doc = mongo.db.opstine.aggregate([match, group, group2, project])
        return json_doc['result']

    def retrieve_list_of_municipalities_for_given_class(self, query_params):
        match = {
            "$match": {
                "tipPodataka.slug": query_params['tipPodataka']
            }
        }
        if query_params['klasifikacijaBroj'] != []:
            query_params['klasifikacijaBroj'] = [str(i) for i in query_params['klasifikacijaBroj']]
            match['$match']["klasifikacija.broj"] = {'$in': query_params['klasifikacijaBroj']}

        # Build group pipeline
        group = {
            "$group": {
                "_id": {
                    "tipPodataka": "$tipPodataka.vrednost",
                    "broj": "$klasifikacija.broj",
                    "opis": "$klasifikacija.opis.latinica",
                },
                'opstine': {
                    "$addToSet": "$opstina.latinica"
                }
            }
        }

        project = {
            "$project": {
                "_id": 0,
                "tipPodataka": "$_id.tipPodataka",
                "klasifikacija": {
                    "broj": "$_id.broj",
                    "opis": "$_id.opis"
                },
                "opstine": "$opstine"

            }
        }

        # Execute mongo request
        json_doc = mongo.db.opstine.aggregate([match, group, project])
        return json_doc['result']