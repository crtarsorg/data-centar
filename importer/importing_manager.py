#coding=utf-8
from csv import reader
import cyrtranslit
from flask_pymongo import MongoClient

# Instantiate mongo database
mongo = MongoClient()

# Create mongo database
db = mongo.datacentar

class ImportingManager(object):

    def __init__(self):
        pass

    def remove_mongo_database(self):
        db.opstine.remove({})

    def data_importer_of_municipality_prijepolje(self):
        pass

    def data_importer_of_municipality_vranje(self):
        pass

    def data_importer_of_municipality_loznica(self):
        pass

    def data_importer_of_municipality_sombor(self):
        pass

    def data_importer_of_municipality_valjevo(self):
        pass

    def data_importer_of_municipality_indjija(self):
        pass

    def data_importer_of_municipality_cacak(self):
        print "cacak"

    def data_importer_of_municipality_krajlevo(self):
        csv_path = "data/krajlevo.csv"
        self.data_importer_of_municipalities_without_parent_handlers(csv_path, "Краљево")

    def data_importer_of_municipality_zvezdara(self):
        csv_path = "data/zvezdara.csv"
        self.data_importer_of_municipalities_with_parent_handlers(csv_path, "Звездара")

    def data_importer_of_municipality_novi_beograd(self):
        csv_path = "data/novi_beograd.csv"
        self.data_importer_of_municipalities_with_parent_handlers(csv_path, "Нови Београд")

    def data_importer_of_municipalities_without_parent_handlers(self, path, opstine):
        db.opstine.remove({})
        data = reader(open(path, "r"), delimiter=',')
        for index, row in enumerate(data):
            if index > 0:
                if row[1] not in ["", " "] and len(row[1]) >= 3:
                    json_doc = self.build_mongo_document_structure(opstine, row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Klasifikacija Broj: %s - Opis: %s" % (opstine, row[1], row[2])

    def data_importer_of_municipalities_with_parent_handlers(self, path, opstine):
        data = reader(open(path, "r"), delimiter=",")

        parent_handler = ''
        for index, row in enumerate(data):
            if index > 0:
                if len(row[1]) == 2:
                    parent_handler = row[2]

                if len(row[1]) > 2 and row[2] not in ["", " "]:
                    json_doc = self.build_mongo_document_structure(opstine, row[1], row[2], row[3], row[4], row[5], row[6], parent_handler, row[1][0:2])
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % (opstine, parent_handler, row[2])

    def build_mongo_document_structure(self, municipality,  class_number, opis, prihodi_vudzeta, sopstveni_prihodi, donacije, ostali, ukupno_k=None,  kategorija_roditelj=None, roditelj_broj=None):

        ukupno = prihodi_vudzeta + sopstveni_prihodi + donacije + ostali
        json_doc = {
            "opstina": {
                "cyrilic": municipality,
                "latin": cyrtranslit.to_latin(municipality, "sr")
            },
            "klasifikacijaBroj": class_number,
            "opis": {
                "latin": cyrtranslit.to_latin(opis, "sr"),
                "cyrilic": opis.strip()
            },
            "prihodiBudzeta": self.convert_to_float(prihodi_vudzeta.replace(',', '').replace('.', '')),
            "sopstveniPrihodi": self.convert_to_float(sopstveni_prihodi.replace(',', '').replace('.', '')),
            "donacije": self.convert_to_float(donacije.replace(',', '').replace('.', '')),
            "ostali": self.convert_to_float(ostali.replace(',', '').replace('.', '')),
            "ukupno": self.convert_to_float(ukupno.replace(',', '').replace('.', ''))
        }

        if municipality in ["Нови Београд", "Звездара"]:
            json_doc["kategorijaRoditelj"] = {
                "opis": kategorija_roditelj,
                "broj": roditelj_broj
            }

        elif municipality in ["Краљево"]:
            json_doc["ukupno"] = self.convert_to_float(ukupno_k.replace(',', '').replace('.', ''))

        return json_doc

    @staticmethod
    def convert_to_float(value):
        if value == " " or value == "":
            value = 0
            return value
        elif value == "000":
            value = 0
            return value
        else:
            return float(value)