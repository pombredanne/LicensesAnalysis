import json

PACKAGES = {}
PERMISSIVITY_INDEX = []

def getLicense(package):
	return PACKAGES[package]["license"]

def getPermissivityIndex(license):
	if license != None:
		license = license.upper()
	for index in range(len(PERMISSIVITY_INDEX)):
		if license in PERMISSIVITY_INDEX[index]:
			return index
	raise Exception
	
def insertLicenseToIndex(license, index):
	if type(index) == str:
		try:
			index = int(index)
		except ValueError as e:
			index = float(index)
			index = int(index)
			PERMISSIVITY_INDEX.insert(index, [])
	if index < 0:
		index = 0
		PERMISSIVITY_INDEX.insert(index, [])
	elif index > len(PERMISSIVITY_INDEX):
		index = len(PERMISSIVITY_INDEX)
		PERMISSIVITY_INDEX.insert(index, [])
	if license != None:
		license = license.upper()
	PERMISSIVITY_INDEX[index].append(license)
	with open("permissivityIndex.json", "w") as permissivityIndex:
		permissivityIndex.write(json.dumps(PERMISSIVITY_INDEX))

def compareLicenses(license1, license2):
	try:
		license1_index = getPermissivityIndex(license1)
	except Exception as e:
		print(PERMISSIVITY_INDEX)
		license1_index = float(input("append license %s to index: " %(license1)))
		insertLicenseToIndex(license1, license1_index)
	try:
		license2_index = getPermissivityIndex(license2)
	except Exception as e:
		print(PERMISSIVITY_INDEX)
		license2_index = input("append license %s to index: " %(license2))
		insertLicenseToIndex(license2, license2_index)
	if license1_index == license2_index:
		return 0
	elif license1_index > license2_index:
		return 1
	elif license1_index < license2_index:
		return -1
	else:
		raise Exception

def isIrregularEdge(edge):
	try:
		license1 = getLicense(edge[0])
		license2 = getLicense(edge[1])
		return compareLicenses(license1, license2) > 0
	except Exception as e:
		return True

def printIrregularEdges():
	for package in PACKAGES:
		dependencies = PACKAGES[package]["dependencies"]
		for dependency in dependencies:
			edge = (package, dependency)
			if isIrregularEdge(edge):
				try:
					print(edge[0], getLicense(package), " --> ", edge[1], getLicense(dependency))
				except Exception as e:
					print(edge[0], " --> ", edge[1])

if __name__ == '__main__':
	with open("dependencyList.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		with open("permissivityIndex.json") as permissivityIndex:
			PERMISSIVITY_INDEX = json.load(permissivityIndex)
		printIrregularEdges()