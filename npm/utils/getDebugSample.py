import json

PACKAGES = {}
DEBUG_PACKAGES = {}
VISITED_PACKAGES = []

def getDependencies(package):
	DEBUG_PACKAGES[package] = PACKAGES[package]
	VISITED_PACKAGES.append(package)
	for dependency in PACKAGES[package]["dependencies"]:
		if dependecy not in VISITED_PACKAGES:
			getDependencies(dependecy)
			
def iteratePackages():
	n = 0
	for package in PACKAGES:
		getDependencies(package)
		n += 1
		if n == 50:
			break

		
if __name__ == '__main__':
	# with open("../data/dependencyList.json") as dependencyList:
	# with open("../data/normalizedDependencyList.json") as dependencyList:
	with open("../../../classifiedDependencyList.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		iteratePackages()
		print(json.dumps(DEBUG_PACKAGES))