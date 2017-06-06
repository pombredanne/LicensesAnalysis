import json
import sys

if __name__ == '__main__':
	with open("data/cranDependencies.json") as dependencyList:
		with open("data/licenses.json") as licensesList:
			licenses = json.load(licensesList)
			with open("data/normalizedLicenses.json") as normalizedLicensesList:
				normalizedLicenses = json.load(normalizedLicensesList)
				packages = json.load(dependencyList)
				for package in packages:
					try:
						packages[package]["license"] = normalizedLicenses[licenses.index(packages[package]["license"])]
					except:
						packages[package]["license"] = "NENHUMA|NO LICENSE"
						
						
		with open("data/normalizedDependencyList.json", "w") as normalizedList:
			normalizedList.write(json.dumps(packages))
