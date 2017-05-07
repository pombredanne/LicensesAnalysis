import json

def getDistribution(packages):
	distribution = {}
	for package in packages:
		try:
			license = packages[package]["license"]
			if license == None:
				license = "None"
			distribution[license] = distribution[license] + 1
		except Exception as e:
			distribution[license] = 1
	return distribution

if __name__ == '__main__':
	with open("dependencyList.json") as dependencyList:
		packages = json.load(dependencyList)
		distribution = getDistribution(packages)
		with open("distribution.json", "w") as distributionList:
			distributionList.write(json.dumps(distribution))