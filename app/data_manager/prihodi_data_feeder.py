# coding=utf-8
from app import mongo
from rashodi_data_feeder import RashodiDataFeed
import re
from bson.regex import Regex

class PrihodiDataFeed():

    def calculate_sum_of_expenditure_types(self, query_params):

        # Build match pipeline
        match = {
            "$match": {
                "tipPodataka.slug": query_params['tipPodataka']
            }
        }

        if "ranges" in query_params:
            ### Let's set the values rage for ukupno ###
            if "ukupno" in query_params["ranges"]:
                match['$match']["ukupno"] = {
                    "$gte": int(query_params["ranges"]["ukupno"]["greaterThanEqual"]),
                    "$lte": int(query_params["ranges"]["ukupno"]["lesserThanEqual"])
                }

            ### Let's set the values rage for sopstveniPrihodi ###
            if "sopstveniPrihodi" in query_params["ranges"]:
                match['$match']["sopstveniPrihodi"] = {
                    "$gte": query_params["ranges"]["sopstveniPrihodi"]["greaterThanEqual"],
                    "$lte": query_params["ranges"]["sopstveniPrihodi"]["lesserThanEqual"]
                }

            ### Let's set the values rage for prihodiBudzeta ###
            if "prihodiBudzeta" in query_params["ranges"]:
                match['$match']["prihodiBudzeta"] = {
                    "$gte": query_params["ranges"]["prihodiBudzeta"]["greaterThanEqual"],
                    "$lte": query_params["ranges"]["prihodiBudzeta"]["lesserThanEqual"]
                }

            ### Let's set the values rage for ostali ###
            if "ostali" in query_params["ranges"]:
                match['$match']["ostali"] = {
                    "$gte": query_params["ranges"]["ostali"]["greaterThanEqual"],
                    "$lte": query_params["ranges"]["ostali"]["lesserThanEqual"]
                }

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

        # Since we use the same mongo query as in Rashodi to build JSON response
        # we use RashdoiDataFeed function, tipPodataka value prihodi determines the difference of json response
        json_doc = RashodiDataFeed().build_json_response_for_parent_categories(query_params)

        return json_doc

    def retrieve_list_of_municipalities_for_given_class(self, query_params):

        # Since we use the same mongo query as in Rashodi to build JSON response
        # we use RashdoiDataFeed function, tipPodataka value prihodi determines the difference of json response
        return RashodiDataFeed().retrieve_list_of_municipalities_for_given_class(query_params)

