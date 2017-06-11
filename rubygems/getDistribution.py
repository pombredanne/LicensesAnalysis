import json
import sys

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
	if len(sys.argv) < 3:
		print("Usage:", sys.argv[0], "<input> <output>")
		sys.exit(1)
	with open(sys.argv[1]) as dependencyList:
		packages = json.load(dependencyList)
		distribution = getDistribution(packages)
		with open(sys.argv[2], "w") as distributionList:
			distributionList.write(json.dumps(distribution))