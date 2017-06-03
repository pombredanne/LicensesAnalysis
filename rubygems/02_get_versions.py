#encoding: utf-8
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import time

URL = "https://rubygems.org/gems/" #name package


def get_versions():
	file = open('data/names_packages.txt', 'r')
	file_versions = open('data/versions.csv', 'w')

	for name in file:
		if (name != ""):
			file_versions.write(name.strip()+',')
			html_page = urllib2.urlopen(URL+name)
			soup = BeautifulSoup(html_page)
			for ol in soup.findAll('ol'):
				for li in ol.findAll('li'):
					if ('gem__versions t-list__items' in ol.get('class')):
						li = li.find("a")
						file_versions.write(li.getText()+ ',')
				file_versions.write("\n")
	file_versions.close()


if __name__ == '__main__':
	start_time = time.time()
	try:
		get_versions()
	except Exception as e:
		print(e)
