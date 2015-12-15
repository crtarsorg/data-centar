#coding=utf-8
import unittest
from importer.data_importer_base import mongo
from importer.utils import ImporterUtils

# Instantiate utils object
utils = ImporterUtils()

class BudzetsImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass

    def get_totals_of_economic_classifications(self):
        for items in utils.total_of_economic_classification_of_budzets():
            yield(items)

    def test_totals_of_economic_classifications(self):
        for i in self.get_totals_of_economic_classifications():
            item = ([x for x in i])
            self.asserts_for_economic_classification_totals(item[0], item[1], item[2], item[3], item[4], item[5])

    def asserts_for_economic_classification_totals(self, razdeo, glava, program, funkcija, programska_aktivnost_projekat, expected_ukupna_sredstva):
        """

        :param razdeo:
        :param glava:
        :param program:
        :param funkcija:
        :param programska_aktivnost_projekat:
        :param ekonomska_klasifikacija:
        :return:
        """
        result = mongo.budzets.aggregate([
            {
                "$match": {
                    "razdeo.broj": razdeo,
                    "glava.broj": glava,
                    "program.broj": program,
                    "funkcija.broj": funkcija,
                    "programskaAktivnostProjekat.broj": programska_aktivnost_projekat
                }
            },
            {
                "$group": {
                    "_id": {
                        "razdeo": "razdeo.broj",
                        "glava": "glava.broj",
                        "program": "program.broj",
                        "funkcija": "funkcija.broj",
                        "programskaAktivnostProjekat": "programskaAktivnostProjekat.broj",
                        "ekonomskaKlasifikacija": "ekonomskaKlasifikacija.broj"

                    },
                    "sum": {
                        "$sum": "$ekonomskaKlasifikacija.ukupna_sredstva"
                    }

                }
            }
        ])

        self.assertEqual(result['result'][0]["sum"], expected_ukupna_sredstva)


