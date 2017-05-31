import json
import sys

PACKAGES = {}
GLOBAL_REGULARITY_RATE = {}

def calculateTree(package):
	globalRegularityRate = PACKAGES[package]["regularityRate"]
	dependencies = PACKAGES[package]["dependencies"]
	for dependency in dependencies:
		try:
			if dependency not in GLOBAL_REGULARITY_RATE.keys():
				calculateTree(dependency)
			globalRegularityRate *= GLOBAL_REGULARITY_RATE[dependency]
		except Exception as e:
			print(e)
	GLOBAL_REGULARITY_RATE[package] = globalRegularityRate

def calculateForest():
	for package in PACKAGES:
		if package not in GLOBAL_REGULARITY_RATE.keys():
			calculateTree(package)
		PACKAGES[package]["globalRegularityRate"] = GLOBAL_REGULARITY_RATE[package]

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("Usage:", sys.argv[0], "<input>", "<output>")
		sys.exit(1)
	with open(sys.argv[1]) as dependencyList:
		PACKAGES = json.load(dependencyList)
		calculateForest()
		with open(sys.argv[2], "w") as regularityRate:
			regularityRate.write(json.dumps(PACKAGES))