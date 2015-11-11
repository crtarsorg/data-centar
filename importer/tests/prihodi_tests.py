#coding=utf-8
import unittest
from importer.prihodi_manager import mongo

class PrihodiImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass

    # Json container for each prijepolje parent category
    prijepolje_counts_of_parents = {
        "Пренети  вишак  прихода из претходне године": 1,
        "ПОРЕЗ НА ДОХ. И КАПИТ.ДОБИТ": 4,
        "ПОРЕЗ  НА  ФОНД  ЗАРАДА": 1,
        "ПОРЕЗ  НА  ИМОВИНУ": 3,
        "ПОРЕЗ  НА  ДОБРА  И  УСЛУГЕ": 3,
        "ДРУГИ   ПОРЕЗИ": 1,
        "ДОНАЦИЈЕ  -  МЕЂУНАРОДНЕ": 1,
        "ТРАНСФЕРИ ОД ДРУГИХ НИВОА ВЛАСТИ": 2,
        "ПРИХОДИ  ОД  ИМОВИНЕ": 3,
        "ПРОДАЈА  ДОБАРА И УСЛУГА": 2,
        "НОВЧАНЕ  КАЗНЕ ЗА  ПРИВРЕДНЕ ПРЕСТУ": 1,
        "МЕШОВИТИ  И  НЕОДРЕЂЕНИ ПРИХОДИ": 1,
        "Меморандумске ставке": 1


    }

    def test_counts_for_parent_categories(self):
        # Test parent counts for municipality of Prijepolje
        for parent in self.prijepolje_counts_of_parents:
            self.asserts_for_parent_categories_elements("Prijepolje", parent, self.prijepolje_counts_of_parents[parent], "prihodi")



    def asserts_for_parent_categories_elements(self, municipality, parent_category, expected_value, data_source):
        '''
        :param municipality: The municipality we want to test
        :param parent_category: The parent category of the elements we want to test
        :param expected_value: The expected value of all the elements of the related parent category
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

