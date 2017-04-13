import json

if __name__ == '__main__':
	index = open("index", "w")
	with open("nodejspackages_05.04.2017.4h.json") as file:
		packages = json.load(file)
		for package in packages:
			index.write(package)
			index.write("\n")
	index.close()