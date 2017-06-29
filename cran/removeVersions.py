import json

file = open("normalizedVersionDependencyList.json")

dependencies = json.load(file)

removed = {}

for package in dependencies:
	for i in range(len(dependencies[package]["dependencies"])):
		dependencies[package]["dependencies"][i] = dependencies[package]["dependencies"][i].split("@")[0]
		removed[package.split("@")[0]] = dependencies[package]

saida = open("output", "w")
saida.write(json.dumps(removed))