# Carregue a Lista de Dependências
# Para cada pacote@versão
#   Para cada Dependência
#     Obtenha seu registro recursivamente
#     Substitua o ID da dependência pela árvore

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
			if dependency not in FOREST_DICTIONARY.keys() and dependency not in VISITED_PACKAGES:
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
	sys.setrecursionlimit(1500)
	with open("dependencyList.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		try:
			buildForest()
		except Exception as e:
			pass
		finally:
			with open("forestList.json", "a") as forestList:
				forestList.write(json.dumps(FOREST_DICTIONARY))