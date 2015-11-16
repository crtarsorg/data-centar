#coding=utf-8
from csv import reader
import cyrtranslit
from flask_pymongo import MongoClient
from utils import ImporterUtils
from slugify import slugify
from abstract_data_importer import DataImporterBase

# Instantiate utils object
utils = ImporterUtils()

# Instantiate mongo client
mongo = MongoClient()

# Create mongo database instance
db = mongo.datacentar

class RashodiDataImporter(object):

    def __init__(self):
        pass

    def data_importer_of_municipality_prijepolje(self):
        db.opstine.remove({"opstina.latinica": "Prijepolje", "tipPodataka.slug": "rashodi"})
        # Read data from vranje csv file
        data_handler = reader(open("data/rashodi/prijepolje.csv", "r"), delimiter=",")
        program = ""
        subprogram = ""
        for index, row in enumerate(data_handler):
            if index > 1:
                if row[1] in ["", " "] and row[2] not in ["", " "] and row[2].strip() in utils.program_categories_for_prijepolje():
                    program = row[2].strip()

                if program != "" and row[2].strip() in utils.program_categories_for_prijepolje()[program]:
                    subprogram = row[2].strip()

                if row[1] not in ["", " "] and len(row[1]) > 2 and program not in ["", " "] and subprogram not in ["", " "]:
                    json_doc = self.build_mongo_document_structure(
                        "Пријепоље",
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        None
                    )
                    json_doc["program"] = {}
                    json_doc["program"]["cirilica"] = program.strip()
                    json_doc["program"]["latinica"] = cyrtranslit.to_latin(program, "sr")
                    json_doc["potProgram"] = {}
                    json_doc["potProgram"]["cirilica"] = subprogram.strip()
                    json_doc["potProgram"]["latinica"] = cyrtranslit.to_latin(subprogram, "sr")
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Program: %s %s" % ("Пријепоље", program, row[1])

    def data_importer_of_municipality_sombor(self):

        # Remove previous records in database, if there is any for this municipality
        db.opstine.remove({"opstina.latinica": "Sombor", "tipPodataka.slug": "rashodi"})

        # Read data from CSV file and assign those data to a data handler object
        data_handler = reader(open("data/rashodi/sombor.csv", "r"), delimiter=",")

        program = ''
        subprogram = ''
        # use program categories for better data categorizing
        program_categories = utils.sombor_programs()
        # Iterate throughout every row in data handler
        for index, row in enumerate(data_handler):
            if index > 6:
                # init program
                if row[2] not in ["", " "]:
                    if row[2].strip() in program_categories:
                        program = row[2].strip()

                    if program != "" and row[2].strip() in program_categories[program]:
                        subprogram = row[2].strip()

                if row[1] not in ["", " "] and program not in ["", " "] and subprogram not in ["", " "] and len(row[1]) < 4:
                    json_doc = self.build_mongo_document_structure(
                        "Сомбор",
                        row[1],
                        row[2].replace("*", ""),
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        None
                    )

                    # Add program and subprogram after building the main mongo document
                    json_doc["program"] = {}
                    json_doc["program"]["cirilica"] = program.strip()
                    json_doc["program"]["latinica"] = cyrtranslit.to_latin(program, "sr")
                    json_doc["potProgram"] = {}
                    json_doc["potProgram"]["cirilica"] = subprogram.strip()
                    json_doc["potProgram"]["latinica"] = cyrtranslit.to_latin(subprogram, "sr")
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Program: %s %s" % ("Сомбор", program, row[1])

    def data_importer_of_municipality_vranje(self):
        db.opstine.remove({"opstina.latinica": "Vranje", "tipPodataka.slug": "rashodi"})
        # init parent categories JSON
        parent_categories = utils.parent_categories_for_vranje()
        program_categories = utils.program_categories_for_vranje()

        # Read data from vranje csv file
        data_handler = reader(open("data/rashodi/vranje.csv", "r"), delimiter=",")
        program = ""
        subprogram = ""
        for index, row in enumerate(data_handler):
            if index > 0:
                if index < 48 and len(row[1]) > 2:
                    if row[1] != "541":
                        parent_handler = parent_categories[row[1][0:2]]
                    else:
                        parent_handler = parent_categories["51"]
                    json_doc = self.build_mongo_document_structure(
                        "Врање",
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        None,
                        parent_handler,
                        row[1][0:2]
                    )
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Врање", parent_handler, row[1])

                elif index > 48:
                    # init program
                    if row[2] not in ["", " "]:
                        if row[2].strip() in program_categories:
                            program = row[2].strip()

                        if program != "" and row[2].strip() in program_categories[program]:
                            subprogram = row[2].strip()

                    if row[1] not in ["", " "] and program not in ["", " "] and subprogram not in ["", " "]:
                        json_doc = self.build_mongo_document_structure(
                            "Врање",
                            row[1],
                            row[2],
                            row[3],
                            row[4],
                            row[5],
                            row[6],
                            None
                        )

                        json_doc["program"] = {}
                        json_doc["program"]["cirilica"] = program.strip()
                        json_doc["program"]["latinica"] = cyrtranslit.to_latin(program, "sr")
                        json_doc["potProgram"] = {}
                        json_doc["potProgram"]["cirilica"] = subprogram.strip()
                        json_doc["potProgram"]["latinica"] = cyrtranslit.to_latin(subprogram, "sr")
                        db.opstine.insert(json_doc)
                        print "Opstine: %s - Program: %s %s" % ("Врање", program, row[1])

    def data_importer_of_municipality_loznica(self):
        db.opstine.remove({"opstina.latinica": "Loznica", "tipPodataka.slug": "rashodi"})
        data_handler = reader(open("data/rashodi/loznica.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if row[1] not in ["", " "]:
                    json_doc = self.build_mongo_document_structure("Лозница", row[1], row[2], row[3], row[4], row[5], row[6], None)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Klasifikacija Broj: %s - Opis: %s" % ("Лозница", row[1], row[2])

    def data_importer_of_municipality_valjevo(self):
        db.opstine.remove({"opstina.latinica": "Valjevo", "tipPodataka.slug": "rashodi"})
        data_handler = reader(open("data/rashodi/valjevo.csv", "r"), delimiter=",")
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
        db.opstine.remove({"opstina.latinica": "Inđija", "tipPodataka.slug": "rashodi"})
        data_handler = reader(open("data/rashodi/indjija.csv", "r"), delimiter=",")
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
        db.opstine.remove({"opstina.latinica": "Čačak", "tipPodataka.slug": "rashodi"})
        data_handler = reader(open("data/rashodi/cacak.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if len(row[1]) > 2 and row[1] not in ["", " "] and row[1] != "4+5":
                    json_doc = self.build_mongo_document_structure("Чачак", row[1], row[2], row[3][:-2], row[4][:-2], row[5][:-2], row[6][:-2], None)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Klasifikacija Broj: %s - Opis: %s" % ("Краљево", row[1], row[2])

    def data_importer_of_municipality_krajlevo(self):
        db.opstine.remove({"opstina.latinica": "Kraljevo", "tipPodataka.slug": "rashodi"})
        data_handler = reader(open("data/rashodi/krajlevo.csv", "r"), delimiter=",")
        for index, row in enumerate(data_handler):
            if index > 0:
                if row[1] not in ["", " "]:
                    json_doc = self.build_mongo_document_structure("Краљево", row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Klasifikacija Broj: %s - Opis: %s" % ("Краљево", row[1], row[2])

    def data_importer_of_municipality_zvezdara(self):
        db.opstine.remove({"opstina.latinica": "Zvezdara"})
        data_handler = reader(open("data/rashodi/zvezdara.csv", "r"), delimiter=",")
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
        db.opstine.remove({"opstina.latinica": "Novi Beograd"})
        data_handler = reader(open("data/rashodi/novi_beograd.csv", "r"), delimiter=",")
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

        if municipality in ["Нови Београд", "Звездара", "Инђија", "Ваљево"]:
            prihodi_vudzeta = self.convert_to_float(prihodi_vudzeta.replace(',', ''))
            sopstveni_prihodi = self.convert_to_float(sopstveni_prihodi.replace(',', ''))
            donacije = self.convert_to_float(donacije.replace(',', ''))
            ostali = self.convert_to_float(ostali.replace(',', ''))
            ukupno = prihodi_vudzeta + sopstveni_prihodi + donacije + ostali

        elif municipality in ["Краљево"]:
            # In this municipality we have values only for column ukupno (total value)
            # That's why we need to import, instead of manually calculating manually
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
            "tipPodataka": {
                "vrednost": "Rashodi",
                "slug": "rashodi",
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

