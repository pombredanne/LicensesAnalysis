#encoding: utf-8
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import json

#Parser de pacotes com dependência, versão e licença do repositório de pacotes do cran

PACKAGES = {}

def get_dependencies():
	file = open('data/names_packages.txt', 'r')
	i = 0

	for name in file:
		if (name != ""):
			html_page = urllib2.urlopen("https://cran.r-project.org/web/packages/"+name)
			name = name.replace('\n', '')
			soup = BeautifulSoup(html_page)
			name_version = ""

			for table in soup.findAll('table'):
				
				for tr in table.findAll('tr'):
					td = tr.findAll('td')
					if (td[0].getText() == "Version:"):
						name_version = name+"@"+td[1].getText().replace('\n', '')
						PACKAGES[name_version] = {"index":0,"package":"","license":"","dependencies":[]}
					elif (td[0].getText() == "Depends:"):
						dependencies = []
						if ("," in td[1].getText()):
							dependencies = td[1].getText().replace('\n', '').split(",")
						else:
							dependencies = td[1].getText().replace('\n', '')
						PACKAGES[name_version]["dependencies"] = dependencies
					elif (td[0].getText() == "License:"):
						if ("," in td[1].getText()):
							license = td[1].getText().replace('\n', '').split(",")
						else:
							license = td[1].getText().replace('\n', '')
						PACKAGES[name_version]["license"] = license
					PACKAGES[name_version]["index"] = i
					PACKAGES[name_version]["package"] = name
		
		#if (i == 2): #para executar o teste em três casos
		#	return None;
		i += 1

if __name__ == '__main__':
	try:
		get_dependencies()
	except Exception as e:
		print(e)
	finally:
		with open("data/cranDependencies.json", "w") as dependencies:
					dependencies.write(json.dumps(PACKAGES))
