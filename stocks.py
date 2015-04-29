import urllib2
import json

"""
Place stock symbols here, they map to a dictionary
that will be filled with current stock information.
The second dictionary will be filled with
{SYMBOL:CHANGPERCENT} mappings that we care about for
the purposes of this project.
"""

symbols = ["AAPL", "NFLX", "GOOG"]

stocks = {}
changePercent = {}

def main():
	update()

def update():
	for symbol in symbols:
		request = 'http://dev.markitondemand.com/Api/v2/Quote/jsonp?symbol=' + symbol + '&callback=convertToDict'
		company = requestCompany(request)
		# Store all of this imformation just in case.
		stocks[symbol] = company
		# For this project, probably only want one value. Keep this separately.
		changePercent[symbol] = company["ChangePercent"]
	return stocks

def requestCompany(request):
	response = urllib2.urlopen(request)

	str_response = response.read().decode("utf-8")

	# evaluation creates call to convertToDict (API specific).
	my_dict = eval(str_response)

	return my_dict

def convertToDict(jsons):
	# jsons is now a python dict.
	return jsons

if __name__ == "__main__":
	main()