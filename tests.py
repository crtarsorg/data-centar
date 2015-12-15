import argparse
from coverage import coverage
import unittest
import os

from importer.tests.rashodi import RashodiImportingTestCases
from importer.tests.prihodi import PrihodiImportingTestCases
from importer.tests.budzets import BudzetsImportingTestCases



# configure code coverage options, omit what you want to exclude from coverage
cov = coverage(branch=True, omit=['venv/*', 'importer/*', '*/tests.py', '*/test.py'])

# Start coverage
cov.start()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--coverage", action='store_true', default=False, help='Execute test coverage: [%(default)s].')

    args = parser.parse_args()

    try:
        suites = []
        # Importer test suites.
        suites.append(unittest.TestLoader().loadTestsFromTestCase(RashodiImportingTestCases))
        suites.append(unittest.TestLoader().loadTestsFromTestCase(PrihodiImportingTestCases))
        suites.append(unittest.TestLoader().loadTestsFromTestCase(BudzetsImportingTestCases))

        # run test cases
        test_cases = unittest.TestSuite(suites)
        unittest.TextTestRunner().run(test_cases)

    except: pass

    # stop and save code coverage
    cov.stop()
    cov.save()


    if args.coverage:

        print("\n\nCode Coverage Report:\n")
        cov.report()

        # get app root directory
        par_dir = os.path.join(__file__, os.pardir)
        par_dir_abs_path = os.path.abspath(par_dir)
        app_dir = os.path.dirname(par_dir_abs_path)

        print("HTML version: " + os.path.join(app_dir, "coverage/index.html"))
        cov.html_report(directory='coverage')
        cov.erase()

