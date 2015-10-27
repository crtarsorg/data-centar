import argparse
from importing_manager import ImportingManager

importer = ImportingManager()

def main_importer(municipalities):

    mun_list = municipalities.split(",")

    for mun in mun_list:

        if mun == "all" or "pripolje":
            importer.data_importer_of_municipality_pripolje()

        if mun == "all" or "vranje":
            importer.data_importer_of_municipality_vranje()

        if mun == "all" or "loznitsa":
            importer.data_importer_of_municipality_loznitsa()

        if mun == "all" or "sombor":
            importer.data_importer_of_municipality_sombor()

        if mun == "all" or "valjevo":
            importer.data_importer_of_municipality_valjevo()

        if mun == "all" or "indjija":
            importer.data_importer_of_municipality_indjija()

        if mun == "all" or "cacak":
            importer.data_importer_of_municipality_cacak()

        if mun == "all" or "krajlevo":
            importer.data_importer_of_municipality_krajlevo()

        if mun == "all" or "zavezdara":
            importer.data_importer_of_municipality_zavezdara()

        if mun == "all" or "novi_beograd":
            importer.data_importer_of_municipality_novi_beograd()


if __name__ == '__main__':

    # Initialize arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--municipalities", help="The data source we want to import")
    args = parser.parse_args()

    # Read the arguments and run the function
    municipalities_sr = args.municipalities
    main_importer(municipalities_sr)