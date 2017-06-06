# Leia o índice
# Para cada pacote do índice
#   Obtenha seus metadados
#   Para cada versão do pacote
#     Grave em disco o JSON

import json
import os
import requests

REGISTRY_URL = 'https://rubygems.org/api/v2/rubygems/'
DEPENDENCY_LIST = None
INDEX = 0

def fetchDependencies(package, version):
	global INDEX
	try:
		req = requests.get(os.path.join(REGISTRY_URL, package, "versions", version + ".json"))
		if req.status_code != 200:
			raise Exception
		metadata = json.loads(req.text)
		registry = {}
		registry["package"] = package
		registry["version"] = version
		try:
			registry["license"] = metadata["licenses"]
		except Exception as e:
			registry["license"] = []
			print(e)
		dependenciesArray = []
		try:
			for dependency in metadata["dependencies"]["runtime"]:
				dependencyName = dependency["name"]
				dependencyVersion = dependency["requirements"]
				dependenciesArray.append(dependencyName+"@"+dependencyVersion)
		except Exception as e:
			print(e)
		finally:
			registry["dependencies"] = dependenciesArray
			registry["index"] = INDEX
			if INDEX > 0:
				DEPENDENCY_LIST.write(",")
				DEPENDENCY_LIST.write("\n")
			DEPENDENCY_LIST.write("\""+registry["package"]+"@"+registry["version"]+"\":")
			DEPENDENCY_LIST.write(json.dumps(registry))
			INDEX += 1
	except Exception as e:
		print(e)

def fetchVersions(line):
	split = line.split(" ")
	package = split[0]
	versions = split[1].split(",")
	for version in versions:
		fetchDependencies(package, version)

if __name__ == '__main__':
	limit = 0
	visitedPackages = open("data/visitedPackages", "w")
	DEPENDENCY_LIST = open("data/dependencyList.json", "w")
	DEPENDENCY_LIST.write("{")
	with open("data/index") as packages:
		packages.readline()
		packages.readline()
		for package in packages:
			package = package[:-1]
			fetchVersions(package)
			visitedPackages.write(package)
			visitedPackages.write("\n")
			limit += 1
			if limit == 10:
				break
	DEPENDENCY_LIST.write("}")
	DEPENDENCY_LIST.close()
	visitedPackages.close()