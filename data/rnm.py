import os, csv

body_array = ['MD', 'CI', 'JCP', 'GP', 'CC', 'UT', 'SP', 'IBD', 'CDI', 'CE', 'AS', 'C', 'X', 'CS', 'CO', 'SA', 'SME']
area_arr = ["S"]

abbrevationLegislature = '62'

for path, dirs, files in os.walk("/home/endrit/Desktop/dev/quien-compro/static/testdata/expenditures"):
	for filename in files:
		os.chdir(path)
		new_name = filename.replace("_62_", "")
		os.rename(filename, new_name)
