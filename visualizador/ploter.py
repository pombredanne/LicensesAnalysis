import json
import os
from igraph import *
#path = '../formatoDados/formatoFinal/listaDependencias.json'
#path = '../formatoDados/debugSamples/debugClassifiedSample.json'
path = '../../classifiedDependencyList.json'
metadata = ""
g = Graph()

def getJson():
	json_file = open(path,'r')	
	metadata = json.loads(json_file.read())
	return metadata
	#for packageName in metadata:
	#	print(packageName)
	#Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]
	#package = metadata["2@2"]
	#print(package["dependencies"])
	#print((metadata["2@2"])[dependencies])
	
def mountTree(head, node, color):
	#print(g.vs.find(name=node))
	try:
		g.vs.find(name=node)
	except:
		try:
			jnode = metadata[node]
			g.add_vertex(name=node, color=color)
		except:
			pass
	#print(metadata[head])
	try:
		dependencies = getDependencies(jnode)
		color = getNodeColor(jnode)
		for package in dependencies:
			package_name = package["package"]
			mountTree(node,package_name, color)
		if head != "":
			print("entrouu")
			relation_ship_type = package["isIrregular"]
			if relation_ship_type == "false":
				edge_color = "blue"
			else:
				edge_color = "red"
			g.add_edges([(g.vs.find(name=node),g.vs.find(name=head))])
	except:
		pass


def getDependencies(package):
	try:
		#print(package['dependencies'])
		return package['dependencies']
	except:
		return []

def getNodeColor(jnode):
	try:
		regularityRate = jnode["regularityRate"]
		if regularityRate == 1:
			return "green"
		elif regularityRate > 0.5:
			return "orange"
		else:
			return "red"
	except:
		return "grey"

if __name__ == '__main__':
	metadata = getJson()
	#node = "1@1.2.1"
	node = "meetup-web-platform@2.0.966-beta"
	#for package in metadata:
	mountTree("", node, "white")
	layout = g.layout("kk")
	plot(g, layout = layout, name=name)