import json

if __name__ == '__main__':
	with open("dependencyList.json") as dependencyList:
		with open("licenses.json") as licensesList:
			licenses = json.load(licensesList)
			with open("normalizedLicenses.json") as normalizedLicensesList:
				normalizedLicenses = json.load(normalizedLicensesList)
				packages = json.load(dependencyList)
				for package in packages:
					packages[package]["license"] = normalizedLicenses[licenses.index(packages[package]["license"])]
		with open("normalizedDependencyList.json", "w") as normalizedList:
			normalizedList.write(json.dumps(packages))