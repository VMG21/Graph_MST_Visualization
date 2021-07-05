# This Python file uses the following encoding: utf-8

#Este programa genera grafos de manera aleatoria y los muestra en pantalla con la ayuda de la libreria random, matplotlib y
#networkx, dependiendo de los valores puede generar grafos conexos o grafos disconexos con "n" numero de nodos.

import networkx as nx
import random
import matplotlib.pyplot as plt
import sys

#Con esta funcion imprimo las conexiones que hay entre un nodos, por ejemplo:
# Nodo 1 esta conectado a nodo 2 y tiene un peso de 5
# 1 - 2  5
def printGraph():
    for (u, v, wt) in G.edges.data('weight'):
        if wt < 100.5:
            print(u, v, wt)

nodes = random.randint(380, 385) #Numero de nodos
seed = random.randint(20, 90) #Semilla
probability = 1 #Probabilidad de que un nodo este conectado a otro
G = nx.gnp_random_graph(nodes, probability, seed, False)

#Le asigna pesos a las aristas de manera aleatoria con valores de entre 1 y 100
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = random.randint(1, 100)

#Tamaño de la ventana donde se muestra el grafo
plt.figure(figsize=(150, 80))

#Se añade la etiqueta de peso a las aristas del grafo
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print("Num. of nodes: ", nodes)

print("First Node - Second Node - Weight")

printGraph()

sys.stdout = open("outFile.txt", "w")
printGraph()
sys.stdout.close()

#Guarda el grafo como imagen y muestra en una ventana el grafo
#Debido a que genera grafos muy densos se recomienda usar plt.show() solo con
#grafos de tamaño menor a 20 para una mejor visualizacion
plt.savefig("filename.png")
plt.show()
