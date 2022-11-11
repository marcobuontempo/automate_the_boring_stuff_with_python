#! python3
# read_census_data.py - A demo program to import and use the data generated from "read_census_excel.py"

import census2010
census2010.all_data["AK"]["Anchorage"]
anchorage_pop = census2010.all_data["AK"]["Anchorage"]["pop"]
print("The 2010 population of Anchorage was " + str(anchorage_pop))
