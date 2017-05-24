import json

PACKAGES = {}
DEBUG_PACKAGES = {}

def getDependencies(package):
	DEBUG_PACKAGES[package] = PACKAGES[package]
	for dependency in PACKAGES[package]["dependencies"]:
		try:
			getDependencies(PACKAGES[dependency]["dependencies"])
		except Exception as e:
			pass

def iteratePackages():
	n = 0
	for package in PACKAGES:
		getDependencies(package)
		n += 1
		if n == 500:
			break

		
if __name__ == '__main__':
	# with open("../data/dependencyList.json") as dependencyList:
	# with open("../data/normalizedDependencyList.json") as dependencyList:
	with open("../data/classifiedDependencyList.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		iteratePackages()
		print(json.dumps(DEBUG_PACKAGES))