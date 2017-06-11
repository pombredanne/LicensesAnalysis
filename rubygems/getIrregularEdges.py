import json
import sys

PACKAGES = {}
STRONG_COPYLEFT_LICENSES = []

def getLicenseList(package):
	return PACKAGES[package]["license"]

def isIrregularEdge(edge):
	sourceLicenseList = getLicenseList(edge[0])
	targetLicenseList = getLicenseList(edge[1])
	for source in sourceLicenseList:
		for target in targetLicenseList:
			if source not in STRONG_COPYLEFT_LICENSES and target in STRONG_COPYLEFT_LICENSES:
				return True
	return False

def evaluateEdges():
	for package in PACKAGES:
		dependencies = PACKAGES[package]["dependencies"]
		regularityRate = len(dependencies)
		index = 0
		for dependency in dependencies:
			edge = (package, dependency)
			try:
				if isIrregularEdge(edge):
					regularityRate -= 1
					PACKAGES[package]["dependencies"][index] = {"package": PACKAGES[package]["dependencies"][index], "isIrregular": True}
					print(edge[0], getLicenseList(package), " --> ", edge[1], getLicenseList(dependency))
				else:
					PACKAGES[package]["dependencies"][index] = {"package": PACKAGES[package]["dependencies"][index], "isIrregular": False}
			except Exception as e:
				PACKAGES[package]["dependencies"][index] = {"package": PACKAGES[package]["dependencies"][index], "isIrregular": None}
			index += 1
		try:
			PACKAGES[package]["regularityRate"] = regularityRate/len(dependencies)
		except Exception as e:
			PACKAGES[package]["regularityRate"] = 1

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage:", sys.argv[0], "<input>")
		sys.exit(1)
	with open(sys.argv[1]) as dependencyList:
		PACKAGES = json.load(dependencyList)
		with open("data/strongCopyleftList.json") as strongCopyleftList:
			STRONG_COPYLEFT_LICENSES = json.load(strongCopyleftList)
		evaluateEdges()
		with open("data/classifiedDependencyList.json", "w") as classifiedDependencyList:
			classifiedDependencyList.write(json.dumps(PACKAGES))