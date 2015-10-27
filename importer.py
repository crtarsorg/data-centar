import argparse
from importing_manager import ImportingManager

importer = ImportingManager()

def main_importer(municipalities):

    mun_list = municipalities.split(",")

    for mun in mun_list:

        if mun in ["all", "pripolje"]:
            importer.data_importer_of_municipality_pripolje()

        if mun in ["all", "vranje"]:
            importer.data_importer_of_municipality_vranje()

        if mun in ["all", "loznitsa"]:
            importer.data_importer_of_municipality_loznitsa()

        if mun in ["all", "sombor"]:
            importer.data_importer_of_municipality_sombor()

        if mun in ["all", "valjevo"]:
            importer.data_importer_of_municipality_valjevo()

        if mun in ["all", "indjija"]:
            importer.data_importer_of_municipality_indjija()

        if mun in ["all", "cacak"]:
            importer.data_importer_of_municipality_cacak()

        if mun in ["all", "krajlevo"]:
            importer.data_importer_of_municipality_krajlevo()

        if mun in ["all", "zavezdara"]:
            importer.data_importer_of_municipality_zavezdara()

        if mun in ["all", "novi_beograd"]:
            importer.data_importer_of_municipality_novi_beograd()


if __name__ == '__main__':

    # Initialize arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--municipalities", help="The data source we want to import")
    args = parser.parse_args()

    # Read the arguments and run the function
    municipalities_sr = args.municipalities
    main_importer(municipalities_sr)