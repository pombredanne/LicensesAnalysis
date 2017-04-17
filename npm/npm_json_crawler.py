# Leia o índice
# Para cada pacote do índice
#   Obtenha seus metadados
#   Para cada versão do pacote
#     Grave em disco o JSON

import json
import os
import requests

REGISTRY_URL = 'https://registry.npmjs.org'
DEPENDENCY_LIST = None
INDEX = 0

def fetch_dependencies(package):
	global INDEX
	try:
		req = requests.get(os.path.join(REGISTRY_URL, package))
		if req.status_code != 200:
			raise Exception
		metadata = json.loads(req.text)
		for version in metadata["versions"]:
			registry = {}
			registry["package"] = package
			registry["version"] = version
			try:
				registry["license"] = metadata["versions"][version]["license"]
			except Exception as e:
				registry["license"] = None
				print(e)
			dependenciesArray = []
			try:
				for dependency in metadata["versions"][version]["dependencies"]:
					dependencyVersion = metadata["versions"][version]["dependencies"][dependency]
					dependencyVersion = dependencyVersion.replace("~", "")
					dependencyVersion = dependencyVersion.replace("^", "")
					dependencyVersion = dependencyVersion.replace(">", "")
					dependencyVersion = dependencyVersion.replace("<", "")
					dependenciesArray.append(dependency+"@"+dependencyVersion)
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

if __name__ == '__main__':
	limit = 0
	visitedPackages = open("visitedPackages", "w")
	DEPENDENCY_LIST = open("dependencyList.json", "w")
	DEPENDENCY_LIST.write("{")
	with open("index") as packages:
		for package in packages:
			package = package[:-1]
			fetch_dependencies(package)
			visitedPackages.write(package)
			visitedPackages.write("\n")
			limit += 1
			if limit == 50:
				break
	DEPENDENCY_LIST.write("}")
	DEPENDENCY_LIST.close()
	visitedPackages.close()