import json
import os
import requests

REGISTRY_URL = 'https://registry.npmjs.org'

def fetch_dependencies(package):
	registry = {}
	try:
		req = requests.get(os.path.join(REGISTRY_URL, package))
		if req.status_code != 200:
			raise Exception
		metadata = json.loads(req.text)
		for version in metadata["versions"]:
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
					dependenciesArray.append(dependency+"@"+dependencyVersion)
			except Exception as e:
				print(e)
			finally:
				registry["dependencies"] = dependenciesArray
	except Exception as e:
		print(e)
	finally:
		return registry

if __name__ == '__main__':
	limit = 0
	visitedPackages = open("visitedPackages", "w")
	dependencyList = open("dependencyList.json", "w")
	dependencyList.write("{")
	index = 0
	with open("index") as packages:
		for package in packages:
			package = package[:-1]
			registry = fetch_dependencies(package)
			if bool(registry):
				registry["index"] = index
				if index != 0:
					dependencyList.write(",")
					dependencyList.write("\n")
				dependencyList.write("\""+registry["package"]+"@"+registry["version"]+"\":")
				dependencyList.write(json.dumps(registry))
				index += 1
			visitedPackages.write(package)
			visitedPackages.write("\n")
			limit += 1
			if limit == 50:
				break
	dependencyList.write("}")
	dependencyList.close()
	visitedPackages.close()