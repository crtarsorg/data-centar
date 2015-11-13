import argparse
from importer.rashodi_manager import RashodiDataImporter
from importer.prihodi_manager import PrihodiDataImporter

rashodi_importer = RashodiDataImporter()
prihodi_importer = PrihodiDataImporter()

def main_importer(data, municipalities):
    mun_list = municipalities.split(",")
    data_source = data.split(",")

    for mun in mun_list:

        if mun in ["all", "prijepolje"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_prijepolje()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_prijepolje()

        if mun in ["all", "vranje"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_vranje()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_vranje()

        if mun in ["all", "loznica"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_loznica()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_loznica()

        if mun in ["all", "sombor"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_sombor()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_sombor()

        if mun in ["all", "valjevo"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_valjevo()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_valjevo()

        if mun in ["all", "indjija"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_indjija()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_indjija()

        if mun in ["all", "cacak"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_cacak()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_cacak()

        if mun in ["all", "kraljevo"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_krajlevo()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_krajlevo()

        if mun in ["all", "zvezdara"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_zvezdara()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_zvezdara()

        if mun in ["all", "novi_beograd"]:
            for data in data_source:
                if data == "prihodi":
                    prihodi_importer.data_importer_of_municipality_novi_beograd()
                elif data == "rashodi":
                    rashodi_importer.data_importer_of_municipality_novi_beograd()

if __name__ == '__main__':

    # Initialize arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--municipalities", help="The data source we want to import for municipality")
    parser.add_argument("--data", help="The data source we want to import")
    args = parser.parse_args()

    # Read the arguments and run the function
    municipalities_sr = args.municipalities
    data_sr = args.data
    main_importer(data_sr, municipalities_sr)