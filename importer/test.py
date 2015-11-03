#coding=utf-8
import unittest
from importing_manager import mongo

class RashodiImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_novi_beograd_municipality(self):

        self.asserts_for_parent_categories_elements("Novi Beograd", "Расходи за запослене", 7)
        self.asserts_for_parent_categories_elements("Novi Beograd", "Коришћење услуга и роба", 6)
        self.asserts_for_parent_categories_elements("Novi Beograd", "Донације дотације и трансфери", 2)
        self.asserts_for_parent_categories_elements("Novi Beograd", "Социјално осигурање и социјална заштита", 1)
        self.asserts_for_parent_categories_elements("Novi Beograd", "Остали расходи", 3)
        self.asserts_for_parent_categories_elements("Novi Beograd", "Средства резерве", 2)
        self.asserts_for_parent_categories_elements("Novi Beograd", "Основна средства", 3)

    def test_zvezdara_municipality(self):
        self.asserts_for_parent_categories_elements("Zvezdara", "РАСХОДИ ЗА ЗАПОСЛЕНЕ", 6)
        self.asserts_for_parent_categories_elements("Zvezdara", "КОРИШЋЕЊЕ РОБА И УСЛУГА", 6)
        self.asserts_for_parent_categories_elements("Zvezdara", "ОТПЛАТА КАМАТА", 1)
        self.asserts_for_parent_categories_elements("Zvezdara", "ДОНАЦИЈЕ ,ДОТАЦИЈЕ И ТРАНСФЕРИ", 2)
        self.asserts_for_parent_categories_elements("Zvezdara", "ОСНОВНА СРЕДСТВА", 3)
        self.asserts_for_parent_categories_elements("Zvezdara", "ПРАВА ИЗ СОЦИЈАЛНОГ ОСИГУРАЊА", 1)
        self.asserts_for_parent_categories_elements("Zvezdara", "ОСТАЛИ РАСХОДИ", 1)
        self.asserts_for_parent_categories_elements("Zvezdara", "Порези, таксе, казне наметнуте од власти", 3)
        self.asserts_for_parent_categories_elements("Zvezdara", "ОТПЛАТА ГЛАВНИЦЕ", 1)
        self.asserts_for_parent_categories_elements("Zvezdara", "РЕЗЕРВА", 2)

    def asserts_for_parent_categories_elements(self, municipality, parent_category, expected_value):

        result = mongo.datacentar.opstine.find(
            {
                "opstina.latin": municipality,
                "kategorijaRoditelj.opis.cyrilic": parent_category
            }
        ).count()

        self.assertEqual(result, expected_value)


class PrihodiImportingTestCases(unittest.TestCase):
    pass
