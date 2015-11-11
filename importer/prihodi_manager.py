#coding=utf-8
from csv import reader
import cyrtranslit
from flask_pymongo import MongoClient
from slugify import slugify
from abstract_data_importer import AbstractDataImporter

# Instantiate mongo client
mongo = MongoClient()

# Create mongo database instance
db = mongo.datacentar

class PrihodiDataImporter(object):

    def __init__(self):
        pass

    def data_importer_of_municipality_prijepolje(self):
        db.opstine.remove({"opstina.latinica": "Prijepolje", "tipPodataka.slug": "prihodi"})
        # Read data from vranje csv file
        data_handler = reader(open("data/prihodi/prijepolje.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 1:

                if len(row[1]) == 3 or row[1][-3:] == '000':
                    parent_handler = row[2]
                    parent_num = row[1]

                if len(row[1]) > 3 and row[1][-3:] != '000':
                    json_doc = self.build_mongo_document_structure("Пријепоље", row[1], row[2], row[3], row[4], row[5], row[6], None, parent_handler, parent_num)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Пријепоље", parent_handler, row[1])

    def data_importer_of_municipality_vranje(self):

        # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Vranje", "tipPodataka.slug": "prihodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/prihodi/vranje.csv", "r"), delimiter=",")

        # Iterate throughout every row in data handler
        for index, row in enumerate(data_handler):
         if index > 1:

                # Use this check to retrieve parent category from csv file rows
                if len(row[1]) == 3 or row[1][-3:] == '000':
                    parent_handler = row[2]
                    parent_num = row[1]

                if len(row[1]) > 3 and row[1][-3:] != '000' and row[1] not in ["7+8+9", "3+7+8+9", "", " "]:

                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Врање", row[1], row[2], row[3], row[4], row[5], row[6], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Врање", parent_handler, row[1])

    def build_mongo_document_structure(self, municipality, class_number, opis, prihodi_vudzeta, sopstveni_prihodi, donacije, ostali, ukupno,  kategorija_roditelj=None, roditelj_broj=None):
        """

        :param municipality:
        :param class_number:
        :param opis:
        :param prihodi_vudzeta:
        :param sopstveni_prihodi:
        :param donacije:
        :param ostali:
        :param ukupno:
        :param kategorija_roditelj:
        :param roditelj_broj:
        :return:
        """
        prihodi_vudzeta = self.convert_to_float(prihodi_vudzeta.replace(',', ''))
        sopstveni_prihodi = self.convert_to_float(sopstveni_prihodi.replace(',', ''))
        donacije = self.convert_to_float(donacije.replace(',', ''))
        ostali = self.convert_to_float(ostali.replace(',', ''))
        ukupno = prihodi_vudzeta + sopstveni_prihodi + donacije + ostali

        # Let's build mongo document structure
        json_doc = {
            "tipPodataka": {
                "vrednost": "Prihodi",
                "slug": "prihodi",
            },
            "godina": 2015,
             "kategorijaRoditelj": {
                "opis": {
                    "cirilica": "Скупштина општине",
                    "latinica": "Skupština Opštine",
                },
                 "broj": 0
            },
            "opstina": {
                "cirilica": municipality,
                "latinica": cyrtranslit.to_latin(municipality, "sr"),
                "slug": slugify(municipality, to_lower=True)
            },
            "klasifikacija": {
                "broj": int(class_number),
                "opis": {
                    "cirilica": opis.strip(),
                    "latinica": cyrtranslit.to_latin(opis.strip(), "sr")
                }
            },
            "prihodiBudzeta": prihodi_vudzeta,
            "sopstveniPrihodi": sopstveni_prihodi,
            "donacije": donacije,
            "ostali": ostali,
            "ukupno": ukupno
        }

        if kategorija_roditelj is not None:
            json_doc["kategorijaRoditelj"]["opis"]["cirilica"] = kategorija_roditelj.strip()
            json_doc["kategorijaRoditelj"]["opis"]["latinica"] = cyrtranslit.to_latin(kategorija_roditelj, "sr")
            json_doc["kategorijaRoditelj"]["broj"] = int(roditelj_broj)

        return json_doc

    @staticmethod
    def convert_to_float(value):
        if value == " " or value == "":
            return 0

        elif value == "000":
            return 0

        elif value.strip() == "-":
            return 0

        elif value.strip() == "#REF!":
            return 0

        else:
            return float(value)

AbstractDataImporter.register(PrihodiDataImporter)
