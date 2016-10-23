import argparse
from importer.izbori.izbori_importer import IzboriDataImporter

izbori_importer = IzboriDataImporter()

if __name__ == '__main__':

    # Initialize arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--election", help="The election type: parlamentarni or predsjednicki.")
    parser.add_argument("--year", help="They election year.")
    parser.add_argument("--month", help="They election month (in case of presidential).")
    parser.add_argument("--round", help="They election round (in case of presidential).")
    args = parser.parse_args()

    # Read the arguments and run the function
    election_type = args.election
    year = args.year
    month = args.month
    rnd = args.round

    if election_type not in ['parlamentarni', 'predsjednicki']:
        print "Input error: %s. Election type should either be 'parlamentarni' or 'predsjednicki'." % election_type

    elif rnd not in [None, 'prvi', 'drugi']:
        print "Input error: %s. Election round should either be 'prvi' or 'drugi'." % election_type

    else:
        izbori_importer.import_data(election_type, year, month, rnd)
