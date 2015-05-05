import urllib2
from bs4 import BeautifulSoup
import json

"""
"""

def main():
	update()

def update():
	webpage = urllib2.urlopen("http://espn.go.com/mlb/team/_/name/sf/san-francisco-giants")
	soup = BeautifulSoup(webpage)
	txt = soup.get_text()
	i = txt.find('"name":"Giants"')	
	j = i
	while txt[i] != "{":
		i -= 1
	while txt[j] != "}":
		j += 1
	txt = str(txt[i:j+1]).replace("true", "True").replace("false", "False")
	dic = eval(txt)
	print dic
	return dic

def gameday(time):
	return game[time]

game = [
	{"hits":0, "runs":0, "on base":0, "errors":0, "hitsOpp":0, "runsOpp":0, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":1, "runs":0, "on base":1, "errors":0, "hitsOpp":0, "runsOpp":0, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":1, "runs":0, "on base":1, "errors":0, "hitsOpp":0, "runsOpp":0, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":1, "runs":1, "on base":0, "errors":0, "hitsOpp":0, "runsOpp":0, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":1, "runs":1, "on base":0, "errors":0, "hitsOpp":1, "runsOpp":0, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":1, "runs":1, "on base":0, "errors":0, "hitsOpp":1, "runsOpp":0, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":1, "runs":1, "on base":0, "errors":0, "hitsOpp":1, "runsOpp":1, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":2, "runs":2, "on base":0, "errors":0, "hitsOpp":1, "runsOpp":1, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":2, "runs":2, "on base":0, "errors":0, "hitsOpp":1, "runsOpp":1, "on baseOpp":0, "errorsOpp":0, "winner":None},
	{"hits":2, "runs":2, "on base":0, "errors":0, "hitsOpp":1, "runsOpp":1, "on baseOpp":0, "errorsOpp":0, "winner":"SF"}
]

if __name__ == "__main__":
	main()