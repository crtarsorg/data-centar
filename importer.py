import argparse
from importing_manager import ImportingManager

importer = ImportingManager()

def main_importer(municipalities):

    mun_list = municipalities.split(",")

    for mun in mun_list:
        if mun == "all":
            importer.data_importer_of_municipality_cacak()

if __name__ == '__main__':

    # Initialize arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--municipalities", help="The data source we want to import")
    args = parser.parse_args()

    # Read the arguments and run the function
    municipalities_sr = args.municipalities
    main_importer(municipalities_sr)