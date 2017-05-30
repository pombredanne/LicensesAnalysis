import requests
import json
import os
from datetime import datetime

REGISTRY_URL = 'https://registry.npmjs.org'
NORMALIZED_VERSIONS = {}

def parseDate(date):
	date = date.replace("-", " ")
	date = date.replace(".", " ")
	date = date.replace(":", " ")
	date = date.replace("T", " ")
	date = date.replace("Z", "")
	dateVetor = date.split(" ")
	dateVetor[0] = int(dateVetor[0])
	dateVetor[1] = int(dateVetor[1])
	dateVetor[2] = int(dateVetor[2])
	dateVetor[3] = int(dateVetor[3])
	dateVetor[4] = int(dateVetor[4])
	dateVetor[5] = int(dateVetor[5])
	dateReturn = datetime(dateVetor[0], dateVetor[1], dateVetor[2], dateVetor[3], dateVetor[4], dateVetor[5])
	return dateReturn

def getLatestVersion(package):
	req = requests.get(os.path.join(REGISTRY_URL, package))
	if req.status_code != 200:
		raise Exception
	metadata = json.loads(req.text)
	latest = None
	for version in metadata["time"]:
		if version != "modified":
			try:
				date = parseDate(metadata["time"][version])
				if latest == None or date > latest["date"]:
					latest = {"version": version, "date": date}
			except Exception as e:
				print(e)
	return latest["version"]

if __name__ == '__main__':
	with open("data/normalizedDependencyList.json") as dependencyList:
		packages = json.load(dependencyList)
		for package in packages:
			index = 0
			for dependency in packages[package]["dependencies"]:
				pk = dependency.split("@")
				dependencyName = pk[0]
				version = pk[1]
				if version.lower() == "latest" or version == "*":
					if dependency in NORMALIZED_VERSIONS.keys():
						print("replacing", dependency)
						dependency = NORMALIZED_VERSIONS[dependency]
					else:
						try:
							print("fetching", dependency)
							version = getLatestVersion(dependencyName)
							dependency = dependencyName+"@"+version
							NORMALIZED_VERSIONS[dependency] = dependency
						except Exception as e:
							print(e)
					packages[package]["dependencies"][index] = dependency
					print("replaced to", dependency)
				index += 1
		with open("data/normalizedVersionDependencyList.json", "w") as normalizedVersionDependencyList:
			normalizedVersionDependencyList.write(json.dumps(packages))