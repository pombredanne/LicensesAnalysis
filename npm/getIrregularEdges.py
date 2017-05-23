import json

PACKAGES = {}
COPYLEFT_LICENSES = []

def getLicenseList(package):
	return PACKAGES[package]["license"]

def isIrregularEdge(edge):
	try:
		sourceLicenseList = getLicenseList(edge[0])
		targetLicenseList = getLicenseList(edge[1])
		for source in sourceLicenseList:
			for target in targetLicenseList:
				if source not in COPYLEFT_LICENSES and target in COPYLEFT_LICENSES:
					return True
		return False
	except Exception as e:
		print(e)
		return True

def printIrregularEdges():
	for package in PACKAGES:
		dependencies = PACKAGES[package]["dependencies"]
		for dependency in dependencies:
			edge = (package, dependency)
			if isIrregularEdge(edge):
				try:
					print(edge[0], getLicenseList(package), " --> ", edge[1], getLicenseList(dependency))
				except Exception as e:
					print(e)
					pass

if __name__ == '__main__':
	with open("data/normalizedDependencyList.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		with open("data/permissivityIndex.json") as permissivityIndex:
			COPYLEFT_LICENSES = json.load(permissivityIndex)
		printIrregularEdges()