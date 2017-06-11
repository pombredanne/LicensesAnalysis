import json

if __name__ == '__main__':
	with open("data/dependencyList.json") as dependencyList:
		with open("data/licenses.json") as licensesList:
			licenses = json.load(licensesList)
			with open("data/normalizedLicenses.json") as normalizedLicensesList:
				normalizedLicenses = json.load(normalizedLicensesList)
				packages = json.load(dependencyList)
				for package in packages:
					packageLicenses = packages[package]["license"]
					if packageLicenses == None:
						packageLicenses = []
					packages[package]["license"] = []
					for license in packageLicenses:
						packages[package]["license"].append(normalizedLicenses[licenses.index(license)])
		with open("data/normalizedDependencyList.json", "w") as normalizedList:
			normalizedList.write(json.dumps(packages))