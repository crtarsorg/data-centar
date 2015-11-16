# coding=utf-8
import abc
from flask_pymongo import MongoClient
from csv import reader

import cyrtranslit
from slugify import slugify
# Instantiate mongo client
mongo = MongoClient()

# Create mongo database instance
db = mongo.datacentar


class DataImporterBase(object):

    def remove_previous_mongo_docs(self, municipality, data_type):
        db.opstine.remove(
            {
                "tipPodataka.slug": data_type,
                "opstina.slug": municipality
            }
        )


    def retrieve_rows_from_csv_file(self,  municipality, data_type):

        # before getting new data from csv file let's remove current records for this entity in database
        """

        :rtype : object
        """
        self.remove_previous_mongo_docs(municipality, data_type)

        #define file path
        file_path = "data/"+ data_type +"/"+ municipality + ".csv"
        # Read data from vranje csv file
        data_handler = reader(open(file_path, "r"), delimiter=",")

        return data_handler


    def build_mongo_document_structure(self, municipality, class_number, opis, prihodi_vudzeta, sopstveni_prihodi, ostali, ukupno,  kategorija_roditelj=None, roditelj_broj=None):
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
        if municipality in ["Сомбор", "Звездара"]:
            # In this municipality we have values only for column ukupno (total value)
            # That's why we need to import, instead of manually calculating manually
            prihodi_vudzeta = 0
            sopstveni_prihodi = 0
            ostali = 0
            ukupno = self.convert_to_float(ukupno.replace(',', ''))
        elif municipality in ["Краљево"]:
            # In this municipality we have values only for column ukupno (total value)
            # That's why we need to import, instead of manually calculating manually
            prihodi_vudzeta = 0
            sopstveni_prihodi = 0
            ostali = 0
            ukupno = self.convert_to_float(ukupno.replace(',', '').replace('.', '')[:-2])
        elif municipality in ["Нови Београд"]:
            # In this municipality we have values only for column ukupno (total value)
            # That's why we need to import, instead of manually calculating manually
            prihodi_vudzeta = 0
            sopstveni_prihodi = 0
            ostali = 0
            ukupno = self.convert_to_float(ukupno.replace('.', ''))
        else:
            prihodi_vudzeta = self.convert_to_float(prihodi_vudzeta.replace(',', ''))
            sopstveni_prihodi = self.convert_to_float(sopstveni_prihodi.replace(',', ''))
            ostali = self.convert_to_float(ostali.replace(',', ''))
            ukupno = prihodi_vudzeta + sopstveni_prihodi + ostali


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
                "opis": {
                    "cirilica": opis.strip(),
                    "latinica": cyrtranslit.to_latin(opis.strip(), "sr")
                }
            },
            "prihodiBudzeta": prihodi_vudzeta,
            "sopstveniPrihodi": sopstveni_prihodi,
            "ostali": ostali,
            "ukupno": ukupno
        }

        if kategorija_roditelj is not None:
            json_doc["kategorijaRoditelj"]["opis"]["cirilica"] = kategorija_roditelj.strip()
            json_doc["kategorijaRoditelj"]["opis"]["latinica"] = cyrtranslit.to_latin(kategorija_roditelj, "sr")
            json_doc["kategorijaRoditelj"]["broj"] = int(roditelj_broj)

        if class_number != "48+49":
            json_doc["klasifikacija"]["broj"] = int(class_number.strip())
        else:
            json_doc["klasifikacija"]["broj"] = class_number.strip()

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
