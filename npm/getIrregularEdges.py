import json

PACKAGES = {}
COPYLEFT_LICENSES = []

def getLicenseList(package):
	return PACKAGES[package]["license"]

def isIrregularEdge(edge):
	try:
		origemLicenseList = getLicenseList(edge[0])
		destinoLicense = getLicenseList(edge[1])
		for origem in origemLicenseList:
			for destino in destinoLicense:
				if origem not in COPYLEFT_LICENSES and destino in COPYLEFT_LICENSES:
					return True
		return False
	except Exception as e:
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
					pass

if __name__ == '__main__':
	with open("normalizedDependencyList.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		with open("permissivityIndex.json") as permissivityIndex:
			COPYLEFT_LICENSES = json.load(permissivityIndex)
		printIrregularEdges()