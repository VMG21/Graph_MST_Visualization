# This Python file uses the following encoding: utf-8
# Este programa grafica un grafo o un MST dado, con un archivo .txt con el siguiente formato de entrada:
# Primera linea: Numero de nodos
# Segunda linea en adelante: Primer Nodo Segundo Nodo y Peso = 0 1 2
# Por ejemplo:
# 10 #Numero de nodos
# 0 1 3 #Primer nodo - Segundo Nodo - Peso
# 0 2 4
# ...
# 9 10 1

import networkx as nx
import matplotlib.pyplot as plt
import sys


def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return res


filename = sys.argv[-1]
file = open(filename)

with open(filename) as f:
    content = [[int(j) for j in i.split(' ')] for i in f.read().split('\n')]
file.close()

num = convert(content[0])

G = nx.Graph()
G.add_node(num-1)

content.pop(0)

for x in range(len(content)):
    a = content[x][0]
    b = content[x][1]
    c = content[x][2]
    G.add_edge(a, b, weight=c)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.savefig("filename.png")
plt.show()
