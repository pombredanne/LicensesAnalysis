#encoding: utf-8
from BeautifulSoup import BeautifulSoup
import urllib2
import re

def get_name_packages():

	file = open('data/names_packages.txt', 'w')
	
	html_page = urllib2.urlopen("https://cran.r-project.org/web/packages/available_packages_by_name.html")
	soup = BeautifulSoup(html_page)
	
	for link in soup.findAll('a'):
		if ('../../web/packages' in link.get('href')):
			file.write(link.getText()+'\n')
	file.close()


if __name__ == '__main__':
	try:
		get_name_packages()
	except Exception as e:
		print(e)