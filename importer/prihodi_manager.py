#coding=utf-8
from csv import reader
import cyrtranslit
from slugify import slugify
from abstract_data_importer import DataImporterBase, db
from utils import ImporterUtils

# Instantiate utils object
utils = ImporterUtils()

class PrihodiDataImporter(DataImporterBase):

    def __init__(self):
        pass


    def data_importer_of_municipality_prijepolje(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        for index, row in enumerate(rows):
            if index > 1:

                if len(row[1]) == 3 or row[1][-3:] == '000':
                    parent_handler = row[2]
                    parent_num = row[1]

                if len(row[1]) > 3 and row[1][-3:] != '000':
                    json_doc = self.build_mongo_document_structure("Пријепоље", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Пријепоље", parent_handler, row[1])

    def data_importer_of_municipality_vranje(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        # Iterate throughout every row in data handler
        for index, row in enumerate(rows):
            if index > 1 and index < 83:

                # Use this check to retrieve parent category from csv file rows
                if len(row[1]) == 3 or row[1][-3:] == '000' or row[2] in ["ПОРЕЗ НА ДОБРА И УСЛУГЕ"]:
                    if row[1] == "" and row[2] == "ПОРЕЗ НА ДОБРА И УСЛУГЕ":
                        parent_num = 0
                    else:
                        parent_num = row[1]

                    parent_handler = row[2]

                if len(row[1]) > 3 and row[1][-3:] != '000' and row[1] not in ["7+8+9", "3+7+8+9", "", " "]:

                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Врање", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Врање", parent_handler, row[1])
            elif index > 82:
                if row[1] in ["810000", "840000", "910000", "920000"]:
                    parent_num = row[1]
                    parent_handler = row[2]

                if row[1] not in ["810000", "840000", "910000", "920000", "900000", "7+8+9", "3+7+8+9", "", " ", "800000"]:

                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Врање", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Врање", parent_handler, row[1])

    def data_importer_of_municipality_loznica(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        parent_handler = ""
        parent_num = ""
        # Iterate throughout every row in data handler
        for index, row in enumerate(rows):

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

    def data_importer_of_municipality_sombor(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        # Iterate throughout every row in data handler
        for index, row in enumerate(rows):
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

    def data_importer_of_municipality_valjevo(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        parent_categories = utils.prihodi_parent_categories_for_valjevo()
        # Iterate throughout every row in data handler
        for index, row in enumerate(rows):
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

                if row[1] not in ["", " ", "800000", parent_num, "900000", "821001"] or row[1] == "821000":

                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Ваљево", row[1], row[2], row[3], row[4], row[5], None, parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Ваљево", parent_handler, row[1].strip())



    def data_importer_of_municipality_indjija(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        # Iterate throughout every row in data handler
        for index, row in enumerate(rows):
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

    def data_importer_of_municipality_krajlevo(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        parent_categories = utils.prihodi_parent_categories_for_kraljevo()

        # Iterate throughout every row in data handler
        for index, row in enumerate(rows):
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


    def data_importer_of_municipality_cacak(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)
        parent_categories = utils.cacak_parent_catecories()
        # Iterate throughout every row in data handler
        for index, row in enumerate(rows):
            if index > 1:
                if row[1] == "" and row[2] in parent_categories[row[1]]:
                    parent_num = row[1].strip()
                    parent_handler = row[2].strip()

                if row[1] not in ["", " "]:
                    if row[1].strip() in parent_categories.keys():
                        parent_num = row[1].strip()
                        parent_handler = parent_categories[parent_num]


                if row[1] not in ["", parent_categories.keys(), "2", "Економска класификација"]:
                    row[3] = row[3].replace(',00', '').replace('.', '')
                    row[4] = row[4].replace(',00', '').replace('.', '')
                    row[5] = row[5].replace(',00', '').replace('.', '')
                    # Build and insert JSON document in mongo
                    json_doc = self.build_mongo_document_structure(
                        "Чачак", row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        None,
                        None,
                        None
                    )
                    db.opstine.insert(json_doc)
                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Чачак", parent_handler, row[1])


    def data_importer_of_municipality_zvezdara(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        parent_handler = ""
        parent_num = ""
        for index, row in enumerate(rows):

            if index > 0:
                if row[1] == "":
                    row[1] = "0"

                if row[1] != "741000":
                    # Build mongo document
                    json_doc = self.build_mongo_document_structure("Звездара", row[1], row[2], row[3], row[4], row[5], row[6], None, None)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Звездара", row[2], row[1])

    def data_importer_of_municipality_novi_beograd(self, municipality, data_type):

        rows = self.retrieve_rows_from_csv_file(municipality, data_type)

        # Iterate throughout every row in data handler
        for index, row in enumerate(rows):
            if index > 0:
                if len(row[1]) == 2 and row[1] not in ["", " "]:
                    parent_num = row[1].strip()
                    parent_handler = row[2]

                if len(row[1]) != 2 and row[1] not in ["", " "]:
                     # Build mongo document
                    json_doc = self.build_mongo_document_structure("Нови Београд", row[1], row[2], row[3], row[4], row[5], row[6], parent_handler, parent_num)

                    # Insert JSON document in mongo
                    db.opstine.insert(json_doc)

                    print "Opstine: %s - Kategorija Roditelj: %s - Opis: %s" % ("Нови Београд", parent_handler, row[1].strip())
