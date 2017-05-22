
def fetch_names():

	URL = "https://pypi.python.org/pypi"

	try:
		import xmlrpclib
	except ImportError:
		import xmlrpc.client as xmlrpclib

	client = xmlrpclib.ServerProxy(URL)

	# get a list of package names
	packages = client.list_packages()

	return packages

def save_name_packages(packages):
	file = open('name_packages.txt', 'w')
	for package in packages:
		file.write("%s \n" % package)

if __name__ == '__main__':
	packages = fetch_names()
	save_name_packages(packages)
