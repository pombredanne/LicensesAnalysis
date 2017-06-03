import json
import sys

PACKAGES = {}
GLOBAL_REGULARITY_RATE = {}
VISITED_PACKAGES = []

def calculateTree(package):
	VISITED_PACKAGES.append(package)
	globalRegularityRate = PACKAGES[package]["regularityRate"]
	dependencies = PACKAGES[package]["dependencies"]
	for dependency in dependencies:
		try:
			dependencyName = dependency["package"]
			if dependencyName not in VISITED_PACKAGES:
				calculateTree(dependencyName)
			globalRegularityRate *= GLOBAL_REGULARITY_RATE[dependencyName]
		except Exception as e:
			pass
	GLOBAL_REGULARITY_RATE[package] = globalRegularityRate

def calculateForest():
	for package in PACKAGES:
		method = "M:"
		if package not in GLOBAL_REGULARITY_RATE.keys():
			calculateTree(package)
			method = "C:"
		PACKAGES[package]["globalRegularityRate"] = GLOBAL_REGULARITY_RATE[package]
		if GLOBAL_REGULARITY_RATE[package] < 1:
			print(method, "[" + str(len(VISITED_PACKAGES)) + "/" + str(len(PACKAGES.keys())) + "]", '\033[1m' + package + '\033[0m', "\t", "{" + str(len(PACKAGES[package]["dependencies"])) + "}", "\t", PACKAGES[package]["regularityRate"], "->", GLOBAL_REGULARITY_RATE[package])

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("Usage:", sys.argv[0], "<input>", "<output>")
		sys.exit(1)
	with open(sys.argv[1]) as dependencyList:
		PACKAGES = json.load(dependencyList)
		calculateForest()
		with open(sys.argv[2], "w") as regularityRate:
			regularityRate.write(json.dumps(PACKAGES))