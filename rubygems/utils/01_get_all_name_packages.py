#encoding: utf-8
from BeautifulSoup import BeautifulSoup
import urllib2
import re

URL = "https://rubygems.org/gems?letter="
LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#LETTERS = ["B"]
TOTAL_PAGES = 0

def get_name_packages():

	file = open('data/names_packages.txt', 'w')
	

	for letter in LETTERS:
		i = 1
		for i in range(TOTAL_PAGES):
			html_page = urllib2.urlopen(URL+letter+"&page="+str(i))
			soup = BeautifulSoup(html_page)
			for link in soup.findAll('a'):
				if ('/gems' in link.get('href')):
					if (link.get('class')):
						if ('gems__gem' in link.get('class')):
							h2 =  link.find('h2')
							span = h2.find('span')
							h2 =  h2.getText()
							span = span.getText()
							value = h2.replace(span, "")
							file.write(value + '\n')
	file.close()

def get_pages():

	global TOTAL_PAGES


	for letter in LETTERS:
		html_page = urllib2.urlopen("https://rubygems.org/gems?letter="+letter)
		soup = BeautifulSoup(html_page)
		pages = []
		for link in soup.findAll('a'):
			if ('/gems?letter='+letter+'&page=' in link.get('href')):
				pages.append(link.getText())
		last_page = pages[-2]
		last_page = int(last_page)
		last_page += 1
		TOTAL_PAGES = last_page



if __name__ == '__main__':
	try:
		get_pages()
		get_name_packages()
	except Exception as e:
		print(e)