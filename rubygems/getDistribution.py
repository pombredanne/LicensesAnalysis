import json

def getDistribution(packages):
	distribution = {}
	for package in packages:
		licenseList = packages[package]["license"]
		if licenseList == None:
			licenseList = ["none"]
		for license in licenseList:
			try:
				distribution[license] = distribution[license] + 1
			except Exception as e:
				distribution[license] = 1
	return distribution

if __name__ == '__main__':
	with open("data/dependencyList.json") as dependencyList:
		packages = json.load(dependencyList)
		distribution = getDistribution(packages)
		with open("data/distribution.json", "w") as distributionList:
			distributionList.write(json.dumps(distribution))