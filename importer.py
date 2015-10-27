import argparse

def main_importer(municipalities):
    mun_list = municipalities.split(",")

    for mun in mun_list:
        if mun == "all":
            pass
    print "Data Centar on running"

# Run the app
if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--municipality", help="Argument is used to specify which municipality data we want to import")

    municipalities = arg_parser.parse_args()
    main_importer(municipalities)
