import json
import sys
import traceback

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
			if dependencyName not in GLOBAL_REGULARITY_RATE.keys() and dependencyName not in VISITED_PACKAGES:
				calculateTree(dependencyName)
			globalRegularityRate *= GLOBAL_REGULARITY_RATE[dependencyName]
			if GLOBAL_REGULARITY_RATE[dependencyName] < 1:
				print("[" + str(len(VISITED_PACKAGES)) + "/" + str(len(PACKAGES.keys())) + "]", '\033[1m' + dependencyName + '\033[0m', "\t", "{" + len(PACKAGES[dependencyName]["dependencies"]) + "}", "\t", PACKAGES[dependencyName]["regularityRate"], "->", GLOBAL_REGULARITY_RATE[dependencyName])
		except Exception as e:
			pass
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