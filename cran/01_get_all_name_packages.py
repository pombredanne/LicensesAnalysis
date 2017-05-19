from BeautifulSoup import BeautifulSoup
import urllib2
import re

f = open('data/names_packages.txt', 'w')

html_page = urllib2.urlopen("https://cran.r-project.org/web/packages/available_packages_by_name.html")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
	if ('../../web/packages' in link.get('href')):
		#print link.getText()
		f.write(link.getText()+'\n')
f.close()