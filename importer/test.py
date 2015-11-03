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

    def test_kraljevo_municipality(self):
        self.asserts_for_parent_categories_elements("Kraljevo", "Скупштина општине", 37)

    def test_cacak_municipality(self):
        self.asserts_for_parent_categories_elements("Čačak", "Скупштина општине", 35)

    def test_indjija_municipality(self):
        self.asserts_for_parent_categories_elements("Inđija", "РАСХОДИ ЗА ЗАПОСЛЕНЕ", 6)
        self.asserts_for_parent_categories_elements("Inđija", "КОРИШЋЕЊЕ УСЛУГА И РОБА", 6)
        self.asserts_for_parent_categories_elements("Inđija", "АМОРТИЗАЦИЈА И УПОТРЕБА СРЕДСТАВА ЗА РАД", 1)
        self.asserts_for_parent_categories_elements("Inđija", "ОТПЛАТА КАМАТА И ПРАТЕЋИ ТРОШКОВИ ЗАДУЖИВАЊА", 2)
        self.asserts_for_parent_categories_elements("Inđija", "СУБВЕНЦИЈЕ", 2)
        self.asserts_for_parent_categories_elements("Inđija", "ДОНАЦИЈЕ, ДОТАЦИЈЕ И ТРАНСФЕРИ", 3)
        self.asserts_for_parent_categories_elements("Inđija", "СОЦИЈАЛНО ОСИГУРАЊЕ И СОЦИЈАЛНА ЗАШТИТА", 1)
        self.asserts_for_parent_categories_elements("Inđija", "ОСТАЛИ РАСХОДИ", 4)
        self.asserts_for_parent_categories_elements("Inđija", "АДМИНИСТРАТИВНИ ТРАНСФЕРИ ИЗ БУЏЕТА И СРЕДСТВА РЕЗЕРВЕ", 1)
        self.asserts_for_parent_categories_elements("Inđija", "ОСНОВНА СРЕДСТВА", 4)
        self.asserts_for_parent_categories_elements("Inđija", "ЗАЛИХЕ", 1)
        self.asserts_for_parent_categories_elements("Inđija", "ПРИРОДНА ИМОВИНА", 1)
        self.asserts_for_parent_categories_elements("Inđija", "ОТПЛАТА ГЛАВНИЦЕ", 1)
        self.asserts_for_parent_categories_elements("Inđija", "НАБАВКА ФИНАНСИЈСКЕ ИМОВИНЕ", 1)

    def asserts_for_parent_categories_elements(self, municipality, parent_category, expected_value):
        '''
        :param municipality: The municipality we want to test
        :param parent_category: The parent category of the elements we want to test
        :param expected_value: The expected value of all the elements of the related parent category
        :return:
        '''
        result = mongo.datacentar.opstine.find(
            {
                "opstina.latin": municipality,
                "kategorijaRoditelj.opis.cyrilic": parent_category
            }
        ).count()

        self.assertEqual(result, expected_value)


class PrihodiImportingTestCases(unittest.TestCase):
    pass
