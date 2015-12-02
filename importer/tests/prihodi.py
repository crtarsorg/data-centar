#coding=utf-8
import unittest
from importer.abstract_data_importer import mongo

class PrihodiImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass

    # Json container for each valjevo parent category
    novi_beograd_counts_of_parents_and_total = {
        #(count, total) -count is the number of parent categories, -total is the total of that parent category
        "ТЕКУЋИ ПРИХОДИ": (6, 499264973),
        "ДРУГИ ПРИХОДИ": (8, 132364859)
    }

    # Json container for each valjevo parent category
    kraljevo_counts_of_parents_and_total = {
        #(count, total) -count is the number of parent categories, -total is the total of that parent category
        "Порез на доходак, добит и капиталне добитке": (6, None),
        "Порез на имовину":(8,),
        "Порез на добра и услуге": (6,),
        "Други порези": (2,),
        "Донације од иностраних држава": (4, ),
        "Донације од међународних органзација": (4, ),
        "Трансфери од других нивоа власти": (4, ),
        "Приходи од имовине": (13, ),
        "Приходи од продаје добара и услуга": (7, ),
        "Новчане казне и одузета имовинска корист": (8, ),
        "Добровољни трансфери од физичких и правних лица": (4, ),
        "Мешовити и неодређени приходи": (2,),
        "Меморандумске ставке за рефундацију расхода": (2,),
        "Меморандумске ставке за рефундацију расхода из претходне године": (2,),
        "Примања од продаје непокретности": (2, ),
        "Примања од продаје покретне имовине": (2, ),
        "Примања од продаје осталих основних средстава": (2, ),
        "Примања од продаје земљишта": (2, ),
        "Примања од домаћих задужења": (6, ),
        "Примања од продаје домаће финансијске имовине": (4, )
    }


    # Json container for each valjevo parent category
    valjevo_counts_of_parents_and_total = {
        #(count, total) -count is the number of parent categories, -total is the total of that parent category
        "ПОРЕЗ НА ДОХОДАК, ДОБИТ И КАПИТАЛНЕ ДОБИТКЕ": (12, 1084150000),
        "ПОРЕЗ НА ИМОВИНУ": (8, 333000000),
        "ПОРЕЗ НА ДОБРА И УСЛУГЕ": (7, 75300000),
        "ДРУГИ ПОРЕЗИ": (1, 35000000),
        "ДОНАЦИЈЕ ОД МЕЂ. ОРГАНИЗАЦИЈА": (1, 7000000),
        "ТРАНСФЕРИ ОД ДРУГИХ НИВОА ВЛАСТИ": (3, 391340000),
        "ПРИХОДИ ОД ИМОВИНЕ": (11, 85500000),
        "ПРИХОДИ ОД ПРОДАЈЕ ДОБАРА И УСЛУГА": (7, 191406000),
        "НОВЧАНЕ КАЗНЕ И ОДУЗЕТА ИМОВИНСКА КОРИСТ": (2, 22000000),
        "ДОБРОВОЉНИ ТРАНСФЕРИ ОД ФИЗИЧКИХ И ПРАВНИХ ЛИЦА": (2, 6100000),
        "МЕШОВИТИ И НЕОДРЕЂЕНИ ПРИХОДИ": (3, 18000000),
        "МЕМОРАНДУМСКЕ СТАВКЕ ЗА РЕФУНДАЦИЈУ РАСХОДА": (1, 10666000),
        "ПРИХОДИ ИЗ БУЏЕТА": (1, 30000000),
        "ПРИМАЊА ОД ПРОДАЈЕ ОСНОВНИХ СРЕДСТАВА": (2, 0),
        "ПРИМАЊА ОД ПРОДАЈЕ РОБНИХ РЕЗЕРВИ": (2, 3500000),
        "ПРИМАЊА ОД ПРОДАЈЕ ПРИРОДНЕ ИМОВИНЕ": (1, 101500000),
        "ПРИМАЊА ОД ЗАДУЖИВАЊА": (2, 0),
        "ПРИМАЊА ОД ПРОДАЈЕ ФИН. ИМОВИНЕ":(1, 5000000)
    }


    # Json container for each prijepolje parent category
    prijepolje_counts_of_parents_and_total = {
        #(count, total) -count is the number of parent categories, -total is the total of that parent category
        "Пренети  вишак  прихода из претходне године": (1, 50000000),
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
        "Меморандумске ставке": (1, 1800000)
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

    indjija_parent_counts = {
        "ПОРЕЗИ НА ДОХОДАК, ДОБИТ И КАПИТАЛНЕ ДОБИТКЕ": (6, 892800000),
        "ПОРЕЗ НА ИМОВИНУ": (4, 332100000),
        "ПОРЕЗИ НА ДОБРА И УСЛУГЕ": (6, 58000000),
        "ДРУГИ ПОРЕЗИ": (1, 60000000),
        "ДОНАЦИЈЕ ОД МЕЂУНАРОДНИХ ОРГАНИЗАЦИЈА": (2, 1500000),
        "ТРАНСФЕРИ ОД ДРУГИХ НИВОА ВЛАСТИ": (2, 983000000),
        "ПРИХОДИ ОД ИМОВИНЕ": (3, 215000000),
        "ПРИХОДИ ОД ПРОДАЈЕ ДОБАРА И УСЛУГА": (4, 217548000),
        "НОВЧАНЕ КАЗНЕ И ОДУЗЕТА ИМОВИНСКА КОРИСТ": (2, 13000000),
        "ДОБРОВОВОЉНИ ТРАНСФЕРИ ОД ФИЗИЧКИХ И ПРАВНИХ ЛИЦА": (1, 2300000),
        "МЕШОВИТИ И НЕОДРЕЂЕНИ ПРИХОДИ": (1, 87520000),
        "МЕМОРАНДУМСКЕ СТАВКЕ ЗА РЕФУНДАЦИЈУ РАСХОДА": (1, 8200000),
        "ПРИМАЊА ОД ПРОДАЈЕ РОБЕ ЗА ДАЉУ ПРОДАЈУ": (1, 4450000),
        "ПРИМАЊА ОД ПРОДАЈЕ ЗЕМЉИШТА": (1, 156000000),
        "ПРИМАЊА ОД ПРОДАЈЕ ДОМАЋЕ ФИНАНСИЈСКЕ ИМОВИНЕ": (1, 100000)
    }

    zvezdara_counts_for_parents = {
        "711000": (1, 249153253),
        "321000": (1, 24203249),
        "713000": (1, 179884638),
        "741000": (1, 0),
        "742000": (4, 2955929),
        "743000": (1, 350000),
        "745000": (1, 0),
        "0": (1, 536454470),
        "733000": (1, 0),
        "732000": (1, 0),
        "771000": (1, 3500000)
    }

    def test_counts_for_parent_categories(self):
        # Test the counts of a particular parent category for Prijepolje municipality
        for parent in self.prijepolje_counts_of_parents_and_total:
            self.asserts_for_parent_categories_elements("Prijepolje", parent, self.prijepolje_counts_of_parents_and_total[parent][0], "prihodi")

        # Test the counts of a particular parent category for Sombor municipality
        for parent in self.sombor_counts_of_parents_and_total:
            self.asserts_for_parent_categories_elements("Sombor", parent, self.sombor_counts_of_parents_and_total[parent][0], "prihodi")

        # Test the counts of a particular parent category for Inđija municipality
        for parent in self.indjija_parent_counts:
            self.asserts_for_parent_categories_elements("Inđija", parent, self.indjija_parent_counts[parent][0], "prihodi")

        # Test the counts of particular parent category for Valjevo municipality
        for parent in self.valjevo_counts_of_parents_and_total:
            self.asserts_for_parent_categories_elements("Valjevo", parent, self.valjevo_counts_of_parents_and_total[parent][0], "prihodi")
        # Test the counts of a particular parent category for Zvezdara municipality
        for parent in self.zvezdara_counts_for_parents:
            self.asserts_for_classification_categories_elements("Zvezdara", parent, self.zvezdara_counts_for_parents[parent][0], "prihodi")

        # Test the counts of particular parent category for Kraljevo municipality
        for parent in self.kraljevo_counts_of_parents_and_total:
            self.asserts_for_parent_categories_elements("Kraljevo", parent, self.kraljevo_counts_of_parents_and_total[parent][0], "prihodi")

        # Test the counts of particular parent category for Kraljevo municipality
        for parent in self.novi_beograd_counts_of_parents_and_total:
            self.asserts_for_parent_categories_elements("Novi Beograd", parent, self.novi_beograd_counts_of_parents_and_total[parent][0], "prihodi")


    def test_total_sum_for_parent_categories(self):
        # Test how much is the total for every parent categories for Prijepolje municipality
        for parent in self.prijepolje_counts_of_parents_and_total:
            self.asserts_for_total_of_parent_categories("Prijepolje", parent, self.prijepolje_counts_of_parents_and_total[parent][1], "prihodi")

        # Test how much is the total for every parent categories for Sombor municipality
        for parent in self.sombor_counts_of_parents_and_total:
            self.asserts_for_total_of_parent_categories("Sombor", parent, self.sombor_counts_of_parents_and_total[parent][1], "prihodi")

         # Test how much is the total for every parent categories for Inđija municipality
        for parent in self.indjija_parent_counts:
            self.asserts_for_total_of_parent_categories("Inđija", parent, self.indjija_parent_counts[parent][1], "prihodi")

         # Test how much is the total for every parent categories for Inđija municipality
        for parent in self.valjevo_counts_of_parents_and_total:
            self.asserts_for_total_of_parent_categories("Valjevo", parent, self.valjevo_counts_of_parents_and_total[parent][1], "prihodi")

        # Test how much is the total for every parent categories for Inđija municipality
        for parent in self.novi_beograd_counts_of_parents_and_total:
            self.asserts_for_total_of_parent_categories("Novi Beograd", parent, self.novi_beograd_counts_of_parents_and_total[parent][1], "prihodi")

         # Test how much is the total for every parent categories for Zvezdara municipality
        for parent in self.zvezdara_counts_for_parents:
            self.asserts_total_sum_of_classification_categories("Zvezdara", parent, self.zvezdara_counts_for_parents[parent][1], "prihodi")


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


    def asserts_for_classification_categories_elements(self, municipality, parent_category, expected_value, data_source):
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
                "klasifikacija.broj": int(parent_category),
                "tipPodataka.slug": data_source
            }
        ).count()

        self.assertEqual(result, expected_value)

    def asserts_total_sum_of_classification_categories(self, municipality, parent_category, expected_value, data_source):
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
                    "klasifikacija.broj": int(parent_category)
                }
            },
            {
                "$group": {
                    "_id": {
                        "municipality": "$opstina.latinica",
                        "data": "$tipPodataka.slug",
                        "category": "$klasifikacija.broj"
                    },
                    "sum": {
                        "$sum": "$ukupno"
                    }
                }
            }
        ])
        self.assertEqual(result['result'][0]["sum"], expected_value)

