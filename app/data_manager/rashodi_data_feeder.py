# coding=utf-8
from app import mongo


class RashodiDataFeed:

    def request_mongo_json_response(self, query_params):

        # Build match pipeline
        match = {
            "$match": {
                "tipPodataka": query_params['data']
            }
        }

        if query_params['godine'] != []:
            match['$match']["godina"] = {'$in': query_params['godine']}

        if query_params['opstine'] != []:
            match['$match']["opstina.latinica"] = {'$in': query_params['opstine']}

        if query_params['klasifikacijaBroj'] != []:
            match['$match']["klasifikacija.broj"] = {'$in': query_params['klasifikacijaBroj']}

        # Build group pipeline
        group = {
            "$group": {
                "_id": {
                    "opstina": "$opstina.latinica",
                    "godina": "$godina",
                    "tipPodataka": "$tipPodataka"
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
        # Execute mongo request
        json_doc = mongo.db.opstine.aggregate([match, group, project])

        return json_doc['result']
