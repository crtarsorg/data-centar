import argparse

def main_importer(municipalities):
    mun_list = municipalities.split(",")

    for mun in mun_list:
        if mun == "all":

    print "Data Centar on running"

# Run the app
if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser()
    municipalities = arg_parser.add_argument("--municipality")
    main_importer(municipalities)
