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

if __name__ == "__main__":
	main()