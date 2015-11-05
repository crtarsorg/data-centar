#coding=utf-8
import unittest
from importing_manager import mongo

class RashodiImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass
    # Json container for each novi beograd parent category
    novi_beograd_counts_of_parents = {
        "Расходи за запослене": 7,
        "Коришћење услуга и роба": 6,
        "Донације дотације и трансфери": 2,
        "Социјално осигурање и социјална заштита": 1,
        "Остали расходи": 3,
        "Средства резерве": 2,
        "Основна средства": 3
    }

    # Json container for each zvezdara parent category
    zvezdara_counts_of_parents = {
        "РАСХОДИ ЗА ЗАПОСЛЕНЕ": 6,
        "КОРИШЋЕЊЕ РОБА И УСЛУГА": 6,
        "ОТПЛАТА КАМАТА": 1,
        "ДОНАЦИЈЕ ,ДОТАЦИЈЕ И ТРАНСФЕРИ": 2,
        "ОСНОВНА СРЕДСТВА": 3,
        "ПРАВА ИЗ СОЦИЈАЛНОГ ОСИГУРАЊА": 1,
        "ОСТАЛИ РАСХОДИ": 1,
        "Порези, таксе, казне наметнуте од власти": 3,
        "ОТПЛАТА ГЛАВНИЦЕ": 1,
        "РЕЗЕРВА": 2
    }

    # Json container for each indjia parent category
    idjia_counts_of_parents = {
        "РАСХОДИ ЗА ЗАПОСЛЕНЕ": 6,
        "КОРИШЋЕЊЕ УСЛУГА И РОБА": 6,
        "АМОРТИЗАЦИЈА И УПОТРЕБА СРЕДСТАВА ЗА РАД": 1,
        "ОТПЛАТА КАМАТА И ПРАТЕЋИ ТРОШКОВИ ЗАДУЖИВАЊА": 2,
        "СУБВЕНЦИЈЕ": 2,
        "ДОНАЦИЈЕ, ДОТАЦИЈЕ И ТРАНСФЕРИ": 3,
        "СОЦИЈАЛНО ОСИГУРАЊЕ И СОЦИЈАЛНА ЗАШТИТА": 1,
        "ОСТАЛИ РАСХОДИ": 4,
        "АДМИНИСТРАТИВНИ ТРАНСФЕРИ ИЗ БУЏЕТА И СРЕДСТВА РЕЗЕРВЕ": 1,
        "ОСНОВНА СРЕДСТВА": 4,
        "ЗАЛИХЕ": 1,
        "ПРИРОДНА ИМОВИНА": 1,
        "ОТПЛАТА ГЛАВНИЦЕ": 1,
        "НАБАВКА ФИНАНСИЈСКЕ ИМОВИНЕ": 1
    }

    # Json container for each Valjevo parent category
    valjevo_counts_of_parents = {
        "РАСХОДИ ЗА ЗАПОСЛЕНЕ": 8,
        "КОРИШЋЕЊЕ УСЛУГА И РОБА": 6,
        "УПОТРЕБА ОСНОВНИХ СРЕДСТАВА": 5,
        "ОТПЛАТА КАМАТА": 4,
        "СУБВЕНЦИЈЕ": 5,
        "ДОНАЦИЈЕ И ТРАНСФЕРИ": 6,
        "СОЦИЈАЛНА ПОМОЋ": 1,
        "ОСТАЛИ РАСХОДИ": 6,
        "АДМИНИСТРАТИВНИ ТРАНСФЕРИ БУЏЕТА": 6,
        "ОСНОВНА СРЕДСТВА": 5,
        "ЗАЛИХЕ": 4,
        "ПРИРОДНА ИМОВИНА": 3,
        "Неф. Имов. која се фин. из сред. за реализ. нип-а": 1,
        "ОТПЛАТА ГЛАВНИЦЕ": 3,
        "Набавка финансијске имовине": 1
    }

    def test_counts_for_parent_categories(self):
        # Test counts for municipality of Novi Beograd
        for parent in self.novi_beograd_counts_of_parents:
            self.asserts_for_parent_categories_elements("Novi Beograd", parent, self.novi_beograd_counts_of_parents[parent])

        # Test counts for municipality of Zvezdara
        for parent in self.zvezdara_counts_of_parents:
            self.asserts_for_parent_categories_elements("Zvezdara", parent, self.zvezdara_counts_of_parents[parent])

        # Test counts for municipality of Kraljevo
        self.asserts_for_parent_categories_elements("Kraljevo", "Скупштина општине", 37)

        # Test counts for municipality of Čačak
        self.asserts_for_parent_categories_elements("Čačak", "Скупштина општине", 35)

        # Test counts for municipality of Inđija
        for parent in self.idjia_counts_of_parents:
            self.asserts_for_parent_categories_elements("Inđija", parent, self.idjia_counts_of_parents[parent])

        # Test counts for municipality of Valjevo
        for parent in self.valjevo_counts_of_parents:
            self.asserts_for_parent_categories_elements("Valjevo", parent, self.valjevo_counts_of_parents[parent])

        # Test counts for municipality of Loznica
        self.asserts_for_parent_categories_elements("Loznica", "Скупштина општине", 578)

    def asserts_for_parent_categories_elements(self, municipality, parent_category, expected_value):
        '''
        :param municipality: The municipality we want to test
        :param parent_category: The parent category of the elements we want to test
        :param expected_value: The expected value of all the elements of the related parent category
        :return:
        '''
        result = mongo.datacentar.opstine.find(
            {
                "opstina.latinica": municipality,
                "kategorijaRoditelj.opis.cirilica": parent_category
            }
        ).count()

        self.assertEqual(result, expected_value)
