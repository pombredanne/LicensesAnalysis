import json

with open("data/normalizedDependencyList.json") as dependencyList:
	PACKAGES = json.load(dependencyList)
	for package in PACKAGES:
		index = 0
		for dependency in PACKAGES[package]["dependencies"]:
			normalizedDependency = dependency
			normalizedDependency = normalizedDependency.replace(" ", "")
			normalizedDependency = normalizedDependency.replace(">", "")
			normalizedDependency = normalizedDependency.replace("<", "")
			normalizedDependency = normalizedDependency.replace("^", "")
			normalizedDependency = normalizedDependency.replace("=", "")
			normalizedDependency = normalizedDependency.replace("~", "")
			normalizedDependency = normalizedDependency.split(",")[0]
			PACKAGES[package]["dependencies"][index] = normalizedDependency
			index += 1
	with open("data/normalizedVersionDependencyList.json", "w") as normalized:
		normalized.write(json.dumps(PACKAGES))