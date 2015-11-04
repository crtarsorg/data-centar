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
        data_handler = reader(open("data/valjevo.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if row[1] != "" and row[1][2] == "0" and row[1][1] != "0":
                    parent_handler = row[2]
                    parent_num = row[1]

                if row[1] not in ["", " ", "400", "500"] and row[1][2] != "0":
                    json_doc = self.build_mongo_document_structure("Ваљево", row[1], row[2], row[3], row[4], row[5], row[6], None, parent_handler, parent_num)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Ваљево", parent_handler, row[1])

    def data_importer_of_municipality_indjija(self):
        db.opstine.remove({"opstina.latin": "Inđija"})
        data_handler = reader(open("data/indjija.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if len(row[1]) == 2:
                    parent_handler = row[2]
                    parent_num = row[1]

                if len(row[1]) > 2 and row[1] not in ["", " "]:
                    json_doc = self.build_mongo_document_structure("Инђија", row[1], row[2], row[3], row[4], row[5], row[6], None, parent_handler, parent_num)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Инђија", parent_handler, row[2])

    def data_importer_of_municipality_cacak(self):
        db.opstine.remove({"opstina.latin": "Čačak"})
        data_handler = reader(open("data/cacak.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if len(row[1]) > 2 and row[1] not in ["", " "] and row[1] != "4+5":
                    json_doc = self.build_mongo_document_structure("Чачак", row[1], row[2], row[3][:-2], row[4][:-2], row[5][:-2], row[6][:-2], None)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Klasifikacija Broj: %s - Opis: %s" % ("Краљево", row[1], row[2])

    def data_importer_of_municipality_krajlevo(self):
        db.opstine.remove({"opstina.latin": "Kraljevo"})
        data_handler = reader(open("data/krajlevo.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if row[1] not in ["", " "]:
                    json_doc = self.build_mongo_document_structure("Краљево", row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Klasifikacija Broj: %s - Opis: %s" % ("Краљево", row[1], row[2])

    def data_importer_of_municipality_zvezdara(self):
        db.opstine.remove({"opstina.latin": "Zvezdara"})
        data_handler = reader(open("data/zvezdara.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if len(row[1]) == 2 or row[1] == "482":
                    parent_handler = row[2]
                    parent_num = row[1]

                if len(row[1]) > 2 and row[1] != "482":
                    json_doc = self.build_mongo_document_structure("Звездара", row[1], row[2], row[3], row[4], row[5], row[6], None, parent_handler, parent_num)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Звездара", parent_handler, row[2])

    def data_importer_of_municipality_novi_beograd(self):
        db.opstine.remove({"opstina.latin": "Novi Beograd"})
        data_handler = reader(open("data/novi_beograd.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if row[1] == "499" or len(row[1]) == 2:
                        parent_handler = row[2]
                        parent_num = row[1]

                if len(row[1]) > 2 and row[1] != "499":
                    json_doc = self.build_mongo_document_structure("Нови Београд", row[1], row[2], row[3], row[4], row[5], row[6], None, parent_handler, parent_num)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Нови Београд", parent_handler, row[2])

    def build_mongo_document_structure(self, municipality, class_number, opis, prihodi_vudzeta, sopstveni_prihodi, donacije, ostali, ukupno,  kategorija_roditelj=None, roditelj_broj=None):

        if municipality in ["Нови Београд", "Звездара", "Инђија", "Ваљево"]:
            prihodi_vudzeta = self.convert_to_float(prihodi_vudzeta.replace(',', ''))
            sopstveni_prihodi = self.convert_to_float(sopstveni_prihodi.replace(',', ''))
            donacije = self.convert_to_float(donacije.replace(',', ''))
            ostali = self.convert_to_float(ostali.replace(',', ''))
            ukupno = prihodi_vudzeta + sopstveni_prihodi + donacije + ostali

        elif municipality in ["Краљево"]:
            # In this municipality we have values only for column ukupno (total value)
            # That's why we need to import, instead of manually calculating
            prihodi_vudzeta = 0
            sopstveni_prihodi = 0
            donacije = 0
            ostali = 0
            ukupno = self.convert_to_float(ukupno.replace(',', '').replace('.', '')[:-2])

        else:
            prihodi_vudzeta = self.convert_to_float(prihodi_vudzeta.replace(',', '').replace('.', ''))
            sopstveni_prihodi = self.convert_to_float(sopstveni_prihodi.replace(',', '').replace('.', ''))
            donacije = self.convert_to_float(donacije.replace(',', '').replace('.', ''))
            ostali = self.convert_to_float(ostali.replace(',', '').replace('.', ''))
            ukupno = prihodi_vudzeta + sopstveni_prihodi + donacije + ostali

        # Let's build mongo document structure
        json_doc = {
             "kategorijaRoditelj": {
                "opis": {
                    "cyrilic": "Скупштина општине",
                    "latin": "Skupština Opštine",
                },
                 "broj": 0
            },
            "opstina": {
                "cyrilic": municipality,
                "latin": cyrtranslit.to_latin(municipality, "sr")
            },
            "klasifikacijaBroj": int(class_number),
            "opis": {
                "latin": cyrtranslit.to_latin(opis, "sr"),
                "cyrilic": opis.strip()
            },
            "prihodiBudzeta": prihodi_vudzeta,
            "sopstveniPrihodi": sopstveni_prihodi,
            "donacije": donacije,
            "ostali": ostali,
            "ukupno": ukupno
        }

        if kategorija_roditelj is not None:
            json_doc["kategorijaRoditelj"]["opis"]["cyrilic"] = kategorija_roditelj.strip()
            json_doc["kategorijaRoditelj"]["opis"]["latin"] = cyrtranslit.to_latin(kategorija_roditelj, "sr")
            json_doc["kategorijaRoditelj"]["broj"] = int(roditelj_broj)

        return json_doc

    @staticmethod
    def convert_to_float(value):
        if value == " " or value == "":
            value = 0
            return value
        elif value == "000":
            value = 0
            return value
        elif value.strip() == "-":
            value = 0
            return value
        else:
            return float(value)
