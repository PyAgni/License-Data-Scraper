#python imports
import argparse
import json
from pprint import pprint

#project level imports
import scraper.getDetails as getDetails


help = "Example Command: python main.py -dl \"DL-0420110149646\" -dob \"09-02-1976\""

arg_parser = argparse.ArgumentParser(description=help)

arg_parser.add_argument('-dl',
						required=True,
						help='Your Driving License Number in the specified format')
arg_parser.add_argument('-dob',
						required=True,
						help='Your Date Of Birth (dd-mm-yyyy)')

args = arg_parser.parse_args()

dl_no = args.dl
dob = args.dob


def check_validity_dl(dl_no):
	if not len(dl_no)==16:
		return False
	if not dl_no[2]=='-':
		return False

	return True

def check_validity_dob(dob):
	if not len(dob)==10:
		return False
	if not (dob[2]=='-' and dob[5]=='-'):
		return False

	return True


if not check_validity_dl(dl_no):
	print("Please check the lisence number format and try again")

elif not check_validity_dob(dob):
	print("Please check the date of birth format and try again")

else:
  response = getDetails(dl_no,dob).scrape()
  print("Data received ->\n")
  pprint(response)
  if response:
    with open('DriverData.json', 'w') as output:
      json.dump(response, output, indent=1)
      print("\nDriver Details Successfully stored in DriverData.json\n")
