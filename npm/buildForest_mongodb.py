# Carregue a Lista de Dependências
# Para cada pacote@versão
#   Para cada Dependência
#     Obtenha seu registro recursivamente
#     Substitua o ID da dependência pela árvore

import json
import sys
from pymongo import MongoClient

FOREST = None
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
			split = dependency.split("@")
			result = FOREST.find_one({"package":split[0],"version":split[1]})
			if result == None and dependency not in VISITED_PACKAGES:
				buildTree(dependency)
			result = FOREST.find_one({"package":split[0],"version":split[1]})
			if result != None:
				dependencyForests.append(result)
		tree["dependencies"] = dependencyForests
	except Exception as e:
		print(e)
	finally:
		FOREST.insert_one(tree)

def buildForest():
	for package in PACKAGES:
		result = FOREST.find_one({"package":PACKAGES[package]["package"],"version":PACKAGES[package]["version"]})
		if result == None:
			buildTree(package)

if __name__ == '__main__':
	sys.setrecursionlimit(1500)
	with open("dependencyList.json") as dependencyList:
		PACKAGES = json.load(dependencyList)
		client = MongoClient('localhost', 27017)
		db = client.npm_forest
		FOREST = db.forest
		buildForest()