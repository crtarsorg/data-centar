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

    def data_importer_of_municipality_prijepolje(self):
        pass

    def data_importer_of_municipality_vranje(self):
        pass

    def data_importer_of_municipality_loznica(self):
        pass

    def data_importer_of_municipality_sombor(self):
        pass

    def data_importer_of_municipality_valjevo(self):
        db.opstine.remove({"opstina.latin": "Valjevo"})
        csv_path ="data/valjevo.csv"
        self.data_importer_of_municipalities_with_parent_handlers(csv_path, "Ваљево")

    def data_importer_of_municipality_indjija(self):
        db.opstine.remove({"opstina.latin": "Inđija"})
        csv_path ="data/indjija.csv"
        self.data_importer_of_municipalities_with_parent_handlers(csv_path, "Инђија")

    def data_importer_of_municipality_cacak(self):
        db.opstine.remove({"opstina.latin": "Čačak"})
        csv_path = "data/cacak.csv"
        self.data_importer_of_municipalities_without_parent_handlers(csv_path, "Чачак")

    def data_importer_of_municipality_krajlevo(self):
        db.opstine.remove({"opstina.latin": "Kraljevo"})
        csv_path = "data/krajlevo.csv"
        self.data_importer_of_municipalities_without_parent_handlers(csv_path, "Краљево")

    def data_importer_of_municipality_zvezdara(self):
        db.opstine.remove({"opstina.latin": "Zvezdara"})
        csv_path = "data/zvezdara.csv"
        self.data_importer_of_municipalities_with_parent_handlers(csv_path, "Звездара")

    def data_importer_of_municipality_novi_beograd(self):
        db.opstine.remove({"opstina.latin": "Novi Beograd"})
        csv_path = "data/novi_beograd.csv"
        self.data_importer_of_municipalities_with_parent_handlers(csv_path, "Нови Београд")

    def data_importer_of_municipalities_without_parent_handlers(self, path, opstine):
        data = reader(open(path, "r"), delimiter=',')
        for index, row in enumerate(data):
            if index > 0:
                if row[1] not in ["", " "] and len(row[1]) >= 3 and row[1][1] != "+":
                    json_doc = None
                    if opstine == "Чачак":
                        json_doc = self.build_mongo_document_structure(opstine, row[1], row[2], row[3][:-2], row[4][:-2], row[5][:-2], row[6][:-2], row[7][:-2])
                    else:
                        json_doc = self.build_mongo_document_structure(opstine, row[1], row[2], row[3], row[4], row[5], row[6], row[7])

                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Klasifikacija Broj: %s - Opis: %s" % (opstine, row[1], row[2])

    def data_importer_of_municipalities_with_parent_handlers(self, path, opstine):
        data = reader(open(path, "r"), delimiter=",")

        parent_handler = ''
        for index, row in enumerate(data):
            if index > 0:
                if opstine == "Ваљево":
                    if row[1] != "" and row[1][2] == "0" and row[1][1] != "0":
                        parent_handler = row[2]

                if len(row[1]) == 2:
                    parent_handler = row[2]

                if len(row[1]) > 2 and row[2] not in ["", " "] and row[1] != row[1][0:2] + "0":
                    json_doc = self.build_mongo_document_structure(opstine, row[1], row[2], row[3], row[4], row[5], row[6], row[7], parent_handler, row[1][0:2])
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % (opstine, parent_handler, row[2])

    def build_mongo_document_structure(self, municipality,  class_number, opis, prihodi_vudzeta, sopstveni_prihodi, donacije, ostali, ukupno,  kategorija_roditelj=None, roditelj_broj=None):
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

        if municipality in ["Нови Београд", "Звездара", "Инђија", "Ваљево"]:
            json_doc["kategorijaRoditelj"] = {
                "opis": kategorija_roditelj,
                "broj": roditelj_broj
            }
            json_doc["prihodiBudzeta"] = self.convert_to_float(prihodi_vudzeta.replace(',', ''))
            json_doc["sopstveniPrihodi"] = self.convert_to_float(sopstveni_prihodi.replace(',', ''))
            json_doc["donacije"] = self.convert_to_float(donacije.replace(',', ''))
            json_doc["ostali"] = self.convert_to_float(ostali.replace(',', ''))
            json_doc["ukupno"] = self.convert_to_float(ukupno.replace(',', ''))

        elif municipality in ["Краљево"]:
            json_doc["ukupno"] = self.convert_to_float(ukupno.replace(',', '').replace('.', '')[:-2])

        return json_doc

    @staticmethod
    def convert_to_float(value):
        if value == " " or value == "":
            value = 0
            return value
        elif value == "000":
            value = 0
            return value
        elif value == "-" or value == "  -     " or value == " -     " or value == "  -":
            value = 0
            return value
        else:
            return float(value)