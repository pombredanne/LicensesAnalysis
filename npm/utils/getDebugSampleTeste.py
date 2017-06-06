import json

PACKAGES = {}
DEBUG_PACKAGES = {}
VISITED_PACKAGES = []
n = 0
def getDependencies(package):
	try:
		DEBUG_PACKAGES[package] = PACKAGES[package]
		VISITED_PACKAGES.append(package)
		for dependency in PACKAGES[package]["dependencies"]:
			pack = dependency["package"]
			if pack not in VISITED_PACKAGES:
				getDependencies(pack)
	except Exception as e:
		pass
			
			
def iteratePackages():
	n = 0
	for package in PACKAGES:
		#if ("lodash" in package) | ("helmet" in package) | ("react-router" in package) | ("moment" in package):
		if "react-router" in package:
			getDependencies(package)
			n += 1
			if n == 500:
				break
		
if __name__ == '__main__':
	# with open("../data/dependencyList.json") as dependencyList:
	# with open("../data/normalizedDependencyList.json") as dependencyList:
	# with open("../../../classifiedDependencyList.json") as dependencyList:
	with open("../../../globalRegularityRate.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		iteratePackages()
		print(json.dumps(DEBUG_PACKAGES))