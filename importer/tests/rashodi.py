#coding=utf-8
import unittest
from importer.rashodi_manager import mongo

class RashodiImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass
    # Json container for each prijepolje program category

    prijepolje_counts_of_programs = {
        "СКУПШТИНА ОПШТИНЕ- ПРОГРАМ 15-ЛОК.САМОУПРАВА": 11,
        "ПРЕДСЕДНИК ОПШ.ПРОГРАМ 15-ЛОКАЛНА САМОУПРАВА": 16,
        "ОПШТИНСКО ВЕЋЕ ПРОГРАМ 15-ЛОКАЛНА САМОУПРАВА": 9,
        "ОПШТИНСКА  УПРАВА ПРОГРАМ 15-ЛОКАЛНА САМОУПРАВА": 26,
        "ОСНОВНО ОБРАЗОВАЊЕ ПРОГРАМ 9": 1,
        "СРЕДЊЕ ОБРАЗОВАЊЕ ПРОГРАМ 10": 1,
        "ДОМ   КУЛТУРЕ ПРОГРАМ 13-РАЗВОЈ КУЛТУРЕ": 18,
        "МАТИЧНА  БИБЛИОТЕКА ПРОГРАМ 13-РАЗВОЈ КУЛТУРЕ": 16,
        "М  У  З  Е  Ј  ПРОГРАМ 13-РАЗВОЈ КУЛТУРЕ": 15,
        "ИСТОРИЈСКИ АРХИВ ПРОГРАМ 13-РАЗВОЈ КУЛТУРЕ":1,
        "ДЕЧЈИ  ВРТИЋ ПРОГРАМ 8-ПРЕДШК.ВАСП.":16,
        "ЦЕНТАР ЗА СОЦ.РАД ПРОГРАМ 11-СОЦ.И ДЕЧ.ЗАШТИТА":1,
        "РАЗВОЈ ЗАЈЕДНИЦЕ ПРОГРАМ 3-ЛОКАЛНИ ЕКОНОМСКИ РАЗВОЈ": 11,
        "ЈАВНИ РЕД И БЕЗБЕДНОСТ ПРОГРАМ 15-ФУНКЦИОНИСАЊЕ ЛОК. САМОУПРАВЕ": 6,
        "ДИРЕКЦИЈА ЗА ИЗГРАДЊУ ПРОГРАМ 1-ЛОКАЛНИ РАЗВОЈ И ПРОСТОРНО ПЛАНИРАЊЕ": 18,
        "ДИРЕКЦИЈА ЗА ИЗГРАДЊУ ПРОГРАМ 7-ПУТНА ИНФРАСТРУКТУРА":2,
        "KOMУНАЛНА ДЕЛАТНОСТ ПРОГРАМ 2- КОМУНАЛНА ДЕЛАТНОСТ": 5,
        "ЗАШТИТА ЖИВОТНЕ СРЕДИНЕ ПРОГРАМ 6": 1,
        "JAВНА   РАСВЕТА ПРОГРАМ 2-КОМУНАЛНА ДЕЛАТНОСТ": 1,
        "ЛОКАЛНИ  ПРЕВОЗ ПРОГРАМ 2-КОМУНАЛНА ДЕЛАТНОСТ": 1,
        "ИНФОРМИСАЊЕ ПРОГРАМ 15-ЛОКАЛНАСАМОУПРАВА": 1,
        "ТУРИСТИЧКА ОРГАНИЗАЦИЈА ПРОГРАМ 4-РАЗВОЈ РАЗВОЈ ТУРИЗМА": 17,
        "ЗАШТИТА    ЖИВОТНЕ   СРЕДИНЕ ПРОГРАМ 6": 1,
        "РАЗВОЈ ПОЉОПРИВРЕДЕ ПРОГРАМ 5": 2,
        "РАЗВОЈ СПОРТА И ОМЛАДИНЕ ПРОГРАМ 14":1,
        "ДОМ ЗДРАВЉА ПРОГРАМ 12-ПРИМАРНА ЗДРАВСТВЕНА ЗАШТИТА": 1,
        "СОЦ.И ДЕЧИЈА ЗАШТИТА ПРОГРАМ 11": 1,
        "ЦРВЕНИ  КРСТ ПРОГРАМ 11-СОЦИЈАЛНА И ДЕЧИЈА ЗАШТИТА": 1

    }
    # Json container for each sombor program category
    sombor_counts_of_programs = {
        "ПРОГРАМ 15 - ЛОКАЛНА САМОУПРАВА": 342,
        "ПРОГРАМ 9 - ОСНОВНО ОБРАЗОВАЊЕ": 300,
        "ПРОГРАМ 3- ЛОКАЛНИ ЕКОНОМСКИ РАЗВОЈ": 6,
        "ПРОГРАМ 6 - ЗАШТИТА ЖИВОТНЕ СРЕДИНЕ": 3,
        "ПРОГРАМ 2 - КОМУНАЛНА ДЕЛАТНОСТ": 41,
        "ПРОГРАМ 7 - ПУТНА ИНФРАСТРУКТУРА": 2,
        "ПРОГРАМ 1 - ЛОКАЛНИ РАЗВОЈ И ПРОСТОРНО ПЛАНИРАЊЕ": 1,
        "ПРОГРАМ 11 - СОЦИЈАЛНА И ДЕЧИЈА ЗАШТИТА": 14,
        "ПРОГРАМ 13 - РАЗВОЈ КУЛТУРЕ": 117,
        "ПРОГРАМ 14 - РАЗВОЈ СПОРТА И ОМЛАДИНЕ": 42,
        "ПРОГРАМ 8 - ПРЕДШКОЛСКО ОБРАЗОВАЊЕ": 18,
        "ПРОГРАМ 10 - СРЕДЊЕ ОБРАЗОВАЊЕ": 102,
        "ПРОГРАМ 12 - ПРИМАРНА ЗДРАВСТВЕНА ЗАШТИТА": 6,
        "ПРОГРАМ 4 - РАЗВОЈ ТУРИЗМА": 15,
        "ПРОГРАМ 5 - РАЗВОЈ ПОЉОПРИВРЕДЕ": 11,
    }

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

    #Json container for each vranje parent category
    vranje_counts_of_parents = {
        "РАСХОДИ ЗА ЗАПОСЛЕНЕ": 7,
        "КОРИШЋЕЊЕ РОБА И УСЛУГА": 6,
        "НЕГ. КУРС.РАЗЛИКЕ": 1,
        "СУБВЕНЦИЈЕ": 2,
        "ДОТАЦИЈЕ ИЗ БУЏЕТА": 2,
        "СОЦИЈАЛНЕ ПОМОЋИ": 1,
        "ОСТАЛИ РАСХОДИ": 5,
        "РЕЗЕРВЕ": 1,
        "ОСНОВНА СРЕДСТВА У ИЗГРАДЊИ": 6
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

        # Test parent counts for municipality of Vranje
        for parent in self.vranje_counts_of_parents:
            self.asserts_for_parent_categories_elements("Vranje", parent, self.vranje_counts_of_parents[parent], "rashodi")

        # Test counts for municipality of Novi Beograd
        for parent in self.novi_beograd_counts_of_parents:
            self.asserts_for_parent_categories_elements("Novi Beograd", parent, self.novi_beograd_counts_of_parents[parent], "rashodi")

        # Test counts for municipality of Zvezdara
        for parent in self.zvezdara_counts_of_parents:
            self.asserts_for_parent_categories_elements("Zvezdara", parent, self.zvezdara_counts_of_parents[parent], "rashodi")

        # Test counts for municipality of Kraljevo
        self.asserts_for_parent_categories_elements("Kraljevo", "Скупштина општине", 37, "rashodi")

        # Test counts for municipality of Čačak
        self.asserts_for_parent_categories_elements("Čačak", "Скупштина општине", 35, "rashodi")

        # Test counts for municipality of Inđija
        for parent in self.idjia_counts_of_parents:
            self.asserts_for_parent_categories_elements("Inđija", parent, self.idjia_counts_of_parents[parent], "rashodi")

        # Test counts for municipality of Valjevo
        for parent in self.valjevo_counts_of_parents:
            self.asserts_for_parent_categories_elements("Valjevo", parent, self.valjevo_counts_of_parents[parent], "rashodi")

        # Test counts for municipality of Loznica
        self.asserts_for_parent_categories_elements("Loznica", "Скупштина општине", 578, "rashodi")

    def test_counts_for_program_categories(self):
        for program in self.sombor_counts_of_programs:
            self.asserts_for_program_categories_elements("Sombor", program, self.sombor_counts_of_programs[program], "rashodi")

        for program in self.prijepolje_counts_of_programs:
            self.asserts_for_program_categories_elements("Prijepolje", program, self.prijepolje_counts_of_programs[program], "rashodi")

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

    def asserts_for_program_categories_elements(self, municipality, program, expected_value, data_source):

        result = mongo.datacentar.opstine.find(
            {
                "opstina.latinica": municipality,
                "tipPodataka.slug": data_source,
                "program.cirilica": program
            }
        ).count()

        self.assertEqual(result, expected_value)
