from BeautifulSoup import BeautifulSoup
import urllib2
import re
import json


PACKAGES = {}
#PACKAGES["key"] = []
#PACKAGES["key"] = {"index":0}


def get_dependencies():
	f = open('data/names_packages.txt', 'r')
	i = 0
	for name in f:
		if (name != ""):
			html_page = urllib2.urlopen("https://cran.r-project.org/web/packages/"+name)
			#print (name)
			soup = BeautifulSoup(html_page)
			name_version = ""
			for table in soup.findAll('table'):
				for tr in table.findAll('tr'):
					td = tr.findAll('td')
					if (td[0].getText() == "Version:"):
						name_version = name+"@"+td[1].getText()
						PACKAGES[name_version] = {}
						#print (td[0].getText() + td[1].getText())
					#PACKAGES[name_version] = {"package": name}
					elif (td[0].getText() == "Depends:"):
						print (td[1].getText())
						dependencies = []
						#PACKAGES[name_version] = {"ola": 123}
						#PACKAGES[name_version] = {"dependencies": td[1].getText().split(",")}
						if ("," in td[1].getText()):
							dependencies = td[1].getText().split(",")
							PACKAGES[name_version] = {"dependencies": dependencies}
							print("mais de um")
							#print (td[0].getText() + td[1].getText().split(","))
						else:
							dependencies = td[1].getText()
							PACKAGES[name_version] = {"dependencies": dependencies}
							print("so um")
							#print (td[0].getText() + td[1].getText())
					elif (td[0].getText() == "License:"):
						if ("," in td[1].getText()):
							PACKAGES[name_version] = {"license": td[1].getText().split(",")}
							#print (td[0].getText() + td[1].getText().split(","))
						else:
							PACKAGES[name_version] = {"license": td[1].getText()}
							#print (td[0].getText() + td[1].getText())
					PACKAGES[name_version] = {"index": i}
		if (i == 2):
			return None;
		i += 1
				#if ("Version" in link.getText()):
					#print(tr.getText())
if __name__ == '__main__':
	get_dependencies()
	#print (PACKAGES)
	with open("dependencies.json", "w") as dependencies:
				dependencies.write(json.dumps(PACKAGES))