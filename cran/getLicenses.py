import json

def extractLicenses(packages):
	licenses = []
	for package in packages:
		license = packages[package]["license"]
		if license not in licenses:
			licenses.append(license)
	return licenses

if __name__ == '__main__':
	with open("data/cranDependencies.json") as dependencyList:
		packages = json.load(dependencyList)
		licenses = extractLicenses(packages)
		with open("data/licenses.json", "w") as licensesList:
			licensesList.write(json.dumps(licenses))
