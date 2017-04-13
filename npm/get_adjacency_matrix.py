#para montar a matriz de adjacências no disco
#carregue o arquivo listaDependencias.json
#para cada entrada
	#para cada dependência
		#obter seus índices
		#ordená-los
		#percorrer o número de chaves pareado com os índices ordenados
			#inserir um se índice consumido
			#inserir zero caso contrário

import json

if __name__ == '__main__':
	adjacencies = open("adjacencies.csv", "w")
	with open("dependencyList.json") as dependencyList:
		packages = json.load(dependencyList)
		for package in packages:
			try:
				dependencies = packages[package]["dependencies"]
			except Exception:
				dependencies = []
			dependencyIndexes = []
			for dependency in dependencies:
				try:
					dependencyIndexes.append(packages[dependency]["index"])
				except Exception as e:
					print(e)
			dependencyIndexes.sort()
			i = 0
			j = 0
			while i < len(packages.keys()):
				if j < len(dependencyIndexes) and i == dependencyIndexes[j]:
					adjacencies.write("1")
					j += 1
				else:
					adjacencies.write("0")
				i += 1
				if i != len(packages.keys()):
					adjacencies.write(",")
			adjacencies.write("\n")