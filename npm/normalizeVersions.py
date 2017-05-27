import requests
import json

REGISTRY_URL = 'https://registry.npmjs.org'

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
	dateVetor[6] = int(dateVetor[6])
	dateReturn = datetime(dateVetor[0], dateVetor[1], dateVetor[2], dateVetor[3], dateVetor[4], dateVetor[5], dateVetor[6])
	return dateReturn

def getLatestVersion(package):
	req = requests.get(os.path.join(REGISTRY_URL, package))
	if req.status_code != 200:
		raise Exception
	metadata = json.loads(req.text)
	latest = None
	for version in metadata["time"]:
		date = parseDate(metadata["time"][version])
		if latest == None or date > latest["date"]:
			latest = {"version": version, "date": date}
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
					version = getLatestVersion(dependencyName)
					packages[package]["dependencies"][index] = version
				index += 1
		with open("data/normalizedVersionDependencyList.json", "w") as normalizedVersionDependencyList:
			normalizedVersionDependencyList.write(json.dumps(packages))