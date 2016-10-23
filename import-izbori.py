import argparse
from importer.izbori.izbori_importer import IzboriDataImporter

izbori_importer = IzboriDataImporter()

if __name__ == '__main__':

    # Initialize arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--election", help="The election type: parlamentarni or predsjednicki.")
    parser.add_argument("--year", help="They election year.")
    args = parser.parse_args()

    # Read the arguments and run the function
    election_type = args.election
    year = args.year

    if election_type not in ['parlamentarni', 'predsjednicki']:
        print "Input error: %s. Election type should either be 'parlamentarni' or 'predsjednicki'." % election_type
    else:
        izbori_importer.import_data(election_type, year)

