# Leia o índice
# Para cada pacote do índice
#   Obtenha seus metadados
#   Para cada versão do pacote
#     Inclua o registro no dicionário
# Grave o JSON em disco

import json
import os
import requests

REGISTRY_URL = 'https://registry.npmjs.org'
INDEX = 0
DEPENDENCY_DICTIONARY = {}

def fetch_dependencies(package):
	global INDEX
	global DEPENDENCY_DICTIONARY
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
					dependenciesArray.append(dependency+"@"+dependencyVersion)
			except Exception as e:
				print(e)
			finally:
				registry["dependencies"] = dependenciesArray
				registry["index"] = INDEX
				DEPENDENCY_DICTIONARY[registry["package"]+"@"+registry["version"]] = registry
				INDEX += 1
	except Exception as e:
		print(e)

if __name__ == '__main__':
	limit = 0
	visitedPackages = open("visitedPackages", "w")
	with open("index") as packages:
		for package in packages:
			package = package[:-1]
			fetch_dependencies(package)
			visitedPackages.write(package)
			visitedPackages.write("\n")
			limit += 1
			if limit == 50:
				break
	visitedPackages.close()
	dependencyList = open("dependencyList.json", "w")
	dependencyList.write(json.dumps(DEPENDENCY_DICTIONARY))
	dependencyList.close()