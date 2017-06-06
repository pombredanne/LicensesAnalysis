import json
import os
from igraph import *

#path = '../formatoDados/formatoFinal/listaDependencias.json'
#path = '../formatoDados/debugSamples/debugClassifiedSample500Teste.json'
#path = '../../classifiedDependencyList.json'
#path = '../../normalizedVersionDependencyList.json'
path = '../../globalRegularityRate.json'

metadata = ""
edge_color = "black"
g = Graph(directed=True)

def getJson():
	json_file = open(path,'r')	
	metadata = json.loads(json_file.read())
	return metadata
'''	
def mountTree(head, node, color):
	#print(g.vs.find(name=node))
	#print(node)
	try:
		g.vs.find(name=node)
		#g.add_edge(g.vs.find(name=head),g.vs.find(name=node),color="black")
	except:
		try:
			jnode = metadata[node]
			if(color != "white"):
				color = getNodeColor(jnode)
			g.add_vertex(name=node, label=node, color=color)
		except:
			print "Unexpected error2:", sys.exc_info()[0]
			#print(node)
			pass
	#print(metadata[head])
	try:
		dependencies = getDependencies(jnode)
		for package in dependencies:
			package_name = package["package"]
			#package_name = package
			mountTree(node, package_name, "orange")
		if head != "":
			relation_ship_type = package["isIrregular"]
			edge_color = getEdgeColor(relation_ship_type)
			g.add_edge(g.vs.find(name=head),g.vs.find(name=node), color=edge_color)
		#print(node)
	except:
		print "Unexpected error1:", sys.exc_info()[0]
		#print(node)
		pass
'''
def getDependencies(package):
	try:
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

def getEdgeColor(relation_ship_type):
	if relation_ship_type == False:
		edge_color = "green"
	elif relation_ship_type == True:
		edge_color = "red"
	else:
		edge_color = "orange"
	return edge_color

def mountTree(head, node, edge_color):
	try:
		g.vs.find(name=node)
		g.add_edge(g.vs.find(name=head),g.vs.find(name=node), color=edge_color, label="verticee")
	except:
		try:
			jnode = metadata[node]
			color = getNodeColor(jnode)
			g.add_vertex(name=node, label=node, color=color)
			g.add_edge(g.vs.find(name=head),g.vs.find(name=node), color=edge_color, label="verticee")
			try:
				jnode = metadata[node]
				dependencies = getDependencies(jnode)
				for package in dependencies:
					package_name = package["package"]
					relation_ship_type = package["isIrregular"]
					edge_color = getEdgeColor(relation_ship_type)
					mountTree(node, package_name, edge_color)
			except:
				print "Unexpected error3:", sys.exc_info()[0]
		except:
			print "Unexpected error2:", sys.exc_info()[0]

def initTree(head):
	try:
		jnode = metadata[head]
		g.add_vertex(name=head, label=head, color="black", label_color="white")
		dependencies = getDependencies(jnode)
		for package in dependencies:
			package_name = package["package"]
			relation_ship_type = package["isIrregular"]
			edge_color = getEdgeColor(relation_ship_type)
			mountTree(head, package_name, edge_color)
			
	except:
		print "Unexpected error1:", sys.exc_info()[0]
		print "Unexpected error1:", sys.exc_info()[1]
		print "Unexpected error1:", sys.exc_info()[2]


if __name__ == '__main__':
	layout = g.layout("kk")
	visual_style = {}
	visual_style["vertex_size"] = 130
	visual_style["edge_width"] = 5
	visual_style["edge_arrow_size"] = 5
	visual_style["layout"] = layout
	visual_style["bbox"] = (9000, 9000)
	visual_style["margin"] = 100
	
	metadata = getJson()
	#node = "1@1.2.1"
	n = 0
	#package = "react-router@4.0.0"
	for package in metadata:
		if "react" in package:
			initTree(package)
			n += 1
			if n == 50:
				break

	plot(g, **visual_style)



	#plot(g, layout = layout)

