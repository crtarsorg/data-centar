from app import mongo

class MongoUtils():

    def __init__(self):
        pass

    def retrieve_classification_numbers(self, tip_podataka):

        json_doc = mongo.db.opstine.aggregate([
            {
                "$match": {
                    "tipPodataka.slug": tip_podataka
                }
            },
            {
                "$group": {
                    "_id": {
                        "klasifikacijaBroj": "$klasifikacija.broj",
                        "klasifikacijaOpis": "$klasifikacija.opis.latinica"
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "klasifikacijaBroj": "$_id.klasifikacijaBroj",
                    "klasifikacijaOpis": "$_id.klasifikacijaOpis"
                }
            }
        ])

        return json_doc['result']