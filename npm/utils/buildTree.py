import json
import sys

FOREST_DICTIONARY = {}
PACKAGES = {}
VISITED_PACKAGES = []

def buildTree(package):
	VISITED_PACKAGES.append(package)
	if package not in PACKAGES.keys():
		return
	tree = PACKAGES[package].copy()
	try:
		dependencies = tree["dependencies"]
		tree["dependencies"] = None
		dependencyForests = []
		for dependency in dependencies:
			dependencyName = dependency["package"]
			if dependencyName not in FOREST_DICTIONARY.keys() and dependencyName not in VISITED_PACKAGES:
				buildTree(dependencyName)
			if dependencyName in FOREST_DICTIONARY.keys():
				dependencyForests.append(FOREST_DICTIONARY[dependencyName])
		tree["dependencies"] = dependencyForests
	except Exception as e:
		print(e)
	finally:
		FOREST_DICTIONARY[package] = tree

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("Usage:", sys.argv[0], "<input>", "<package>")
		sys.exit(1)
	with open(sys.argv[1]) as dependencyList:
		PACKAGES = json.load(dependencyList)
		buildTree(sys.argv[2])
		print(json.dumps(FOREST_DICTIONARY))