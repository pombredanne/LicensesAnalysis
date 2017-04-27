# Carregue a Lista de Dependências
# Para cada pacote@versão
#   Para cada Dependência
#     Obtenha seu registro recursivamente
#     Substitua o ID da dependência pela árvore

import json

FOREST_DICTIONARY = {}
PACKAGES = {}

def buildTree(package):
	if package not in PACKAGES.keys():
		return
	tree = PACKAGES[package].copy()
	try:
		dependencies = tree["dependencies"]
		tree["dependencies"] = None
		dependencyForests = []
		for dependency in dependencies:
			if dependency not in FOREST_DICTIONARY.keys():
				buildTree(dependency)
			if dependency in FOREST_DICTIONARY.keys():
				dependencyForests.append(FOREST_DICTIONARY[dependency])
		tree["dependencies"] = dependencyForests
	except Exception as e:
		print(e)
	finally:
		FOREST_DICTIONARY[package] = tree

def buildForest():
	for package in PACKAGES:
		if package not in FOREST_DICTIONARY.keys():
			buildTree(package)

if __name__ == '__main__':
	with open("dependencyList.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		buildForest()
		with open("forestList.json", "w") as forestList:
			forestList.write(json.dumps(FOREST_DICTIONARY))