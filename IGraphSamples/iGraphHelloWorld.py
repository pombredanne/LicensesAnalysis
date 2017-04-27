from igraph import *

g = Graph( [ (0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)  ] ) #Cada numero é um vertice, cada conjunto (x,y) é um edge
g.vs["name"] = ["Nakao, the Asian", "Romulo, the Legend", "Marco, the Wild Master", "Pontes, the Great", "Lord Wiese", "Lord Polato", "Testerson"] #Seta um atributo nome para cada elemento, respctivamente para cada um dos 7 vertices do grafo
g.vs["age"] = [22, 21, 21, 21, 30, 40, 777]#Seta um atributo idade para cada elemento, respctivamente para cada um dos 7 vertices do grafo
g.vs["gender"] = ["m","m","m","m","m","m","f"]#Seta um atributo gender para cada elemento, respctivamente para cada um dos 7 vertices do grafo
g.es["isFormal"]=[True,True,True,True,True,True,False]
g.vs["label"] = g.vs["name"]#Atributo usado para o plot
color_dict = {"m": "blue", "f": "pink"}
g.vs["color"] = [color_dict[gender] for gender in g.vs["gender"]]
layout = g.layout("kk")
#plot(g, layout = layout)
plot(g, layout = layout)



