#coding=utf-8
import unittest
from importer.prihodi_manager import mongo

class PrihodiImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass

    # Json container for each prijepolje parent category
    prijepolje_counts_of_parents_and_total = {
        #(count, total) -count is the number of parent categories, -total is the total of that parent category
        "Пренети  вишак  прихода из претходне године": (1, 50996198),
        "ПОРЕЗ НА ДОХ. И КАПИТ.ДОБИТ": (4, 261000000),
        "ПОРЕЗ  НА  ФОНД  ЗАРАДА": (1,1000),
        "ПОРЕЗ  НА  ИМОВИНУ": (3, 45548618),
        "ПОРЕЗ  НА  ДОБРА  И  УСЛУГЕ": (3, 15900000),
        "ДРУГИ   ПОРЕЗИ": (1, 15000000),
        "ДОНАЦИЈЕ  -  МЕЂУНАРОДНЕ": (1, 2000000),
        "ТРАНСФЕРИ ОД ДРУГИХ НИВОА ВЛАСТИ": (2, 521982240),
        "ПРИХОДИ  ОД  ИМОВИНЕ": (3, 5010000),
        "ПРОДАЈА  ДОБАРА И УСЛУГА": (2, 8400000),
        "НОВЧАНЕ  КАЗНЕ ЗА  ПРИВРЕДНЕ ПРЕСТУ": (1,8170800),
        "МЕШОВИТИ  И  НЕОДРЕЂЕНИ ПРИХОДИ": (1, 52205859),
        "Меморандумске ставке": (1, 3600000)


    }

     # Json container for each prijepolje parent category
    sombor_counts_of_parents_and_total = {
        #(count, total) -count is the number of parent categories, -total is the total of that parent category
        "ПОРЕЗИ НА ДОХОДАК, ДОБИТ И КАПИТАЛНЕ ДОБИТКЕ": (5, 1205000000),
        "ПОРЕЗИ НА ИМОВИНУ": (3, 526000000),
        "ПОРЕЗИ НА ДОБРА И УСЛУГЕ": (4, 66000000),
        "КОМУНАЛНА ТАКСА НА ИСТИЦАЊЕ ФИРМЕ": (1, 45000000),
        "ТРАНСФЕРИ ОД ДРУГИХ НИВОА ВЛАСТИ": (2, 409000000),
        "ПРИХОДИ ОД ИМОВИНЕ": (4, 203000000),
        "ПРИХОДИ ОД ПРОДАЈЕ ДОБАРА И УСЛУГА": (3, 97000000),
        "ПРИХОДИ ОД НОВЧАНИХ КАЗНИ": (2, 14000000),
        "МЕШОВИТИ И НЕОДРЕЂЕНИ ПРИХОДИ": (2, 85000000),
        "МЕМОРАНДУМСКЕ СТАВКЕ ЗА РЕФУНДАЦИЈУ РАСХОДА": (1, 2500000),
        "ПРИМАЊА ОД ПРОДАЈЕ ПОКРЕТНЕ ИМОВИНЕ": (1, 500000),
        "ПРИМАЊА ОД ПРОДАЈЕ НЕПОКРЕТНОСТИ": (1, 7000000),
        "ПРИМАЊА ОД ПРОДАЈЕ ДОМАЋЕ ФИНАНС.ИМОВИНЕ": (1, 2000000),
        "ДОНАЦИЈЕ ОД МЕЂУНАРОДНИХ ОРГАНИЗАЦИЈА": (1, 10000000)
    }

    def test_counts_for_parent_categories(self):
        # Test the counts of a particular parent category for Prijepolje municipality
        for parent in self.prijepolje_counts_of_parents_and_total:
            self.asserts_for_parent_categories_elements("Prijepolje", parent, self.prijepolje_counts_of_parents_and_total[parent][0], "prihodi")

        # Test the counts of a particular parent category for Sombor municipality
        for parent in self.sombor_counts_of_parents_and_total:
            self.asserts_for_parent_categories_elements("Sombor", parent, self.sombor_counts_of_parents_and_total[parent][0], "prihodi")


    def test_total_for_parent_categories(self):
        # Test how much is the total for every parent categories for Prijepolje municipality
        for parent in self.prijepolje_counts_of_parents_and_total:
            self.asserts_for_total_of_parent_categories("Prijepolje", parent, self.prijepolje_counts_of_parents_and_total[parent][1], "prihodi")

        # Test how much is the total for every parent categories for Sombor municipality
        for parent in self.sombor_counts_of_parents_and_total:
            self.asserts_for_total_of_parent_categories("Sombor", parent, self.sombor_counts_of_parents_and_total[parent][1], "prihodi")



    def asserts_for_parent_categories_elements(self, municipality, parent_category, expected_value, data_source):
        '''
        :param municipality: The municipality we want to test
        :param parent_category: The parent category for the municipality we want to test
        :param expected_value: The expected value of the number of all elements for that parent category
        :param data_source: The data source, if we want to test for revenues or expenditures
        :return:
        '''
        result = mongo.datacentar.opstine.find(
            {
                "opstina.latinica": municipality,
                "kategorijaRoditelj.opis.cirilica": parent_category,
                "tipPodataka.slug": data_source
            }
        ).count()

        self.assertEqual(result, expected_value)

    def asserts_for_total_of_parent_categories(self, municipality, parent_category, expected_value, data_source):
        """

        :param municipality: The municipality we want to test
        :param parent_category: The parent category for the municipality we want to test
        :param expected_value: The expected value of the total for that parent category
        :param data_source: The data source, if we want to test for revenues or expenditures
        :return:
        """
        result = mongo.datacentar.opstine.aggregate([
            {
                "$match": {
                    "opstina.latinica": municipality,
                    "tipPodataka.slug": data_source,
                    "kategorijaRoditelj.opis.cirilica": parent_category
                }

            },
            {
                "$group": {
                    "_id": {
                        "municipality": "$opstina.latinica",
                        "data": "$tipPodataka.slug",
                        "category": "$kategorijaRoditelj.opis.cirilica"
                    },
                    "sum": {
                        "$sum": "$ukupno"
                    }
                }
            }
        ])
        self.assertEqual(result['result'][0]["sum"], expected_value)

