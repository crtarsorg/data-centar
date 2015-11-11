from abstract_data_importer import AbstractDataImporter

class PrihodiDataImporter(object):

    def convert_to_float(value):
        """
        To be implemented
        :param value:
        :return:
        """
        pass

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
        pass


AbstractDataImporter.register(PrihodiDataImporter)
