import json

with open("normalizedVersionDependencyList.json") as dependencyList:
	PACKAGES = json.load(dependencyList)
	for package in PACKAGES:
		index = 0
		for dependency in PACKAGES[package]["dependencies"]:
			PACKAGES[package]["dependencies"][index] = dependency.replace(">", "").replace("<", "").replace("^", "").replace("=", "").replace("~", "")
			index += 1
	with open("normalizedVersionLimitersDependencyList.json", "w") as normalized:
		normalized.write(json.dumps(PACKAGES))