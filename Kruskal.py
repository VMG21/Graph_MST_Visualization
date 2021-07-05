# This Python file uses the following encoding: utf-8

import os, sys
import time
import networkx as nx
import matplotlib.pyplot as plt

operation = 0

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def agregarArista(self, u, v, w):
        global operation
        self.graph.append([u, v, w])
        operation = operation + 1

    def find(self, parent, i):
        global operation
        if parent[i] == i:
            return i
        operation = operation + 1
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        global operation
        raizx = self.find(parent, x)
        raizy = self.find(parent, y)
        if rank[raizx] < rank[raizy]:
            parent[raizx] = raizy
            operation = operation + 1
        elif rank[raizx] > rank[raizy]:
            parent[raizy] = raizx
            operation = operation + 1
        else:
            parent[raizy] = raizx
            rank[raizx] += 1
            operation = operation + 1

    def kruskal(self):
        result = []
        i, e, cost = 0, 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        global operation

        print("First Node - Second node \tWeight")

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            operation = operation + 1
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            operation = operation + 1
            if x != y:
                e = e + 1
                result.append([u, v, w])
                G.add_edge(u,v, weight=w)
                self.union(parent, rank, x, y)
                operation = operation + 1
        for u, v, weight in result:
            print('{0}\t\t{1}\t  {2}'.format(u, v, weight).expandtabs(10))
            cost += weight
            operation = operation + 1
        print("Total weight: " + str(cost))

# Funcion que convierte una lista en entero
# Recibe como argumento una lista
def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return res


# Empieza el contador
start_time = time.time()

G = nx.Graph()

# Guarda el nombre del .txt como argumento y lo guarda como "filename"
filename = sys.argv[-1]
file = open(filename)

# Se convierte el archivo de texto en una lista y los valores se convierten de str a int
with open(filename) as f:
    content = [[int(j) for j in i.split(' ')] for i in f.read().split('\n')]
file.close()

# Guardo el primer valor del archivo
num = convert(content[0])

# Se crea el grafo con N numero de nodos
g = Grafo(num)
G.add_node(num-1)

content.pop(0)

# Agrego los bordes que hay entre cada nodo
for x in range(len(content)):
    a = content[x][0]
    b = content[x][1]
    c = content[x][2]
    g.agregarArista(a, b, c)
    operation = operation + 1

g.kruskal()

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0.99, hspace=0.995)

figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

print("Numero de operaciones basicas: ", operation)

# Tiempo de ejecución
print("--- %s seconds ---" % (time.time() - start_time))

plt.show()
