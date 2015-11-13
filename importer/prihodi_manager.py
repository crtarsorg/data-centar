#coding=utf-8
from csv import reader
import cyrtranslit
from flask_pymongo import MongoClient
from slugify import slugify
from abstract_data_importer import AbstractDataImporter
from utils import ImporterUtils

# Instantiate utils object
utils = ImporterUtils()

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
                    json_doc = self.build_mongo_document_structure("Пријепоље", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)
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
                    json_doc = self.build_mongo_document_structure("Врање", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Врање", parent_handler, row[1])

    def data_importer_of_municipality_loznica(self):

        # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Loznica", "tipPodataka.slug": "prihodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/prihodi/loznitsa.csv", "r"), delimiter=",")

        parent_handler = ""
        parent_num = ""
        # Iterate throughout every row in data handler
        for index, row in enumerate(data_handler):

            if index > 1:
                # Use this check to retrieve parent category from csv file rows
                if row[1][-3:] == '000' and row[1][-4:] not in ["00000", "0000"]:
                    parent_handler = row[2]
                    parent_num = row[1]

                if row[1][-3:] != '000' and row[1] not in ["", " "]:

                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Лозница", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Лозница", parent_handler, row[1])

    def data_importer_of_municipality_sombor(self):

        # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Sombor", "tipPodataka.slug": "prihodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/prihodi/sombor.csv", "r"), delimiter=",")

        # Iterate throughout every row in data handler
        for index, row in enumerate(data_handler):
            if index > 0:
                 # Use this check to retrieve parent category from csv file rows
                 if row[1][-3:] == "000" and row[1] not in ["", " "]:
                     parent_handler = row[2]
                     parent_num = row[1]

                 if row[1][-3:] != "000" and row[1] not in ["", " "]:
                     # Build mongo document
                        json_doc = self.build_mongo_document_structure("Сомбор", row[1], row[2], row[3], row[4], row[5], row[6], parent_handler, parent_num)

                        # Insert JSON document in mongo
                        db.opstine.insert(json_doc)

                        print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Сомбор", parent_handler, row[1])

    def data_importer_of_municipality_valjevo(self):
        # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Valjevo", "tipPodataka.slug": "prihodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/prihodi/valjevo.csv", "r"), delimiter=",")

        parent_categories = utils.prihodi_parent_categories_for_valjevo()
        # Iterate throughout every row in data handler
        for index, row in enumerate(data_handler):
            if index > 3 and index < 79:
                # Use this check to retrieve parent category from csv file rows
                if row[1][-3:] == "000" and row[1][-4:] != "0000" and row[2] not in ["Приходи од  продаје  индиректних корисника буџета"]:
                    parent_handler = row[2]
                    parent_num = row[1]

                if row[1][-3:] != "000" and row[1] not in ["", " "] or row[2] in ["Приходи од  продаје  индиректних корисника буџета"]:

                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Ваљево", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Ваљево", parent_handler, row[1].strip())
            elif index > 78 and index:
                if row[1] not in ["", " "]:
                    if row[1].strip() in parent_categories.keys():
                        parent_num = row[1].strip()
                        parent_handler = parent_categories[parent_num]

                if row[1] not in ["", " ", "800000", parent_num, "900000"] or row[2] in ["ПРИМАЊА ОД ПРОДАЈЕ РОБНИХ РЕЗЕРВИ"]:

                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Ваљево", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Ваљево", parent_handler, row[1].strip())



    def data_importer_of_municipality_indjija(self):
        # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Inđija", "tipPodataka.slug": "prihodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/prihodi/indija.csv", "r"), delimiter=",")

        # Iterate throughout every row in data handler
        for index, row in enumerate(data_handler):
            if index > 0:
                 # Use this check to retrieve parent category from csv file rows
                 if row[1] in ["", " "] and row[2] not in ["", "УКУПНИ ПРИХОДИ И ПРИМАЊА БУЏЕТА"]:
                     parent_handler = row[2]
                     parent_num = 0

                 elif row[1] != "":
                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Инђија", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Инђија", parent_handler, row[1])

    def data_importer_of_municipality_krajlevo(self):
         # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Kraljevo", "tipPodataka.slug": "prihodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/prihodi/kraljevo.csv", "r"), delimiter=",")

        parent_categories = utils.prihodi_parent_categories_for_kraljevo()

        # Iterate throughout every row in data handler
        for index, row in enumerate(data_handler):
            if index > 2:
                if row[1] not in ["", " "]:
                    if row[1].strip() in parent_categories.keys():
                        parent_num = row[1].strip()
                        parent_handler = parent_categories[parent_num]

                if row[1] not in ["", " ", parent_num] and row[1][-4:] != "0000":

                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Краљево", row[1], row[2], row[3], row[4], row[5], row[6], parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Краљево", parent_handler, row[1].strip())


    def data_importer_of_municipality_cacak(self):
        '''
        # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Čačak", "tipPodataka.slug": "rashodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/prihodi/cacak.csv", "r"), delimiter=",")

        # Iterate throughout every row in data handler
        for index, row in enumerate(data_handler):
            if index > 0:
                if row[1][-3:] == "000" and row[1][-4:] != "0000":
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Чачак", parent_handler, row[1])

        '''
        pass

    def data_importer_of_municipality_zvezdara(self):

        # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Zvezdara", "tipPodataka.slug": "prihodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/prihodi/zvezdara.csv", "r"), delimiter=",")

        parent_handler = ""
        parent_num = ""
        for index, row in enumerate(data_handler):

            if index > 0:
                if row[1] == "":
                    row[1] = "0"

                # Build mongo document
                json_doc = self.build_mongo_document_structure("Звездара", row[1], row[2], row[3], row[4], row[5], row[6], None, None)

                # Insert JSON document in mongo
                db.opstine.insert(json_doc)

                print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Звездара", parent_handler, row[1])


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
                "broj": int(class_number.strip()),
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
