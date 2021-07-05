# This Python file uses the following encoding: utf-8
import os, sys
import time
import networkx as nx
import matplotlib.pyplot as plt


class Grafo:
    # Constructor de la clase Grafo
    def __init__(self, numNodos):
        self.m_v = numNodos
        self.m_arista = []
        self.m_componente = {}

    # Esta funcion añade una nueva arista a nuestro grafo
    # Recibe como argumentos: (Primer nodo, segundo nodo, peso del borde)
    def agregarArista(self, u, v, peso):
        global operation
        self.m_arista.append([u, v, peso])
        operation = operation + 1

    def buscarComponente(self, u):
        global operation
        if self.m_componente[u] == u:
            return u
        operation = operation + 1
        return self.buscarComponente(self.m_componente[u])

    # En este método, trataremos el diccionario como un árbol.
    # Preguntamos si hemos encontrado o no la raíz de nuestro componente.
    # Si no hemos encontrado el nodo raíz, buscamos de forma recursiva el padre del nodo actual.
    # Recibe como argumento un nodo
    def set_component(self, u):
        if self.m_componente[u] == u:
            return
        else:
            for k in self.m_componente.keys():
                self.m_componente[k] = self.buscarComponente(k)

    # Este método unifica dos componentes en uno, dados dos nodos que pertenecen a sus respectivas componentes
    # Recibe como argumentos: (tamaño del componente, primer nodo, segundo nodo)
    def union(self, component_size, u, v):
        global operation
        if component_size[u] <= component_size[v]:
            self.m_componente[u] = v
            component_size[v] += component_size[u]
            self.set_component(u)
            operation = operation + 1

        elif component_size[u] >= component_size[v]:
            self.m_componente[v] = self.buscarComponente(u)
            component_size[u] += component_size[v]
            self.set_component(v)
            operation = operation + 1

    def boruvka(self):
        # Lista de componentes
        sizeComponente = []
        # Se inicializa el tamaño del peso del minimo arbol recubridor en cero
        pesoMST = 0
        global operation

        minimum_weight_edge = [-1] * self.m_v

        for nodo in range(self.m_v):
            self.m_componente.update({nodo: nodo})
            sizeComponente.append(1)
            operation = operation + 1
        numComponents = self.m_v

        print("First Node - Second node \tWeight")
        while numComponents > 1:
            for i in range(len(self.m_arista)):

                u = self.m_arista[i][0]
                v = self.m_arista[i][1]
                w = self.m_arista[i][2]

                componente_u = self.m_componente[u]
                componente_v = self.m_componente[v]

                if componente_u != componente_v:
                    if minimum_weight_edge[componente_u] == -1 or \
                            minimum_weight_edge[componente_u][2] > w:
                        minimum_weight_edge[componente_u] = [u, v, w]
                        operation = operation + 1
                    if minimum_weight_edge[componente_v] == -1 or \
                            minimum_weight_edge[componente_v][2] > w:
                        minimum_weight_edge[componente_v] = [u, v, w]
                        operation = operation + 1
            operation = operation + 1

            for nodo in range(self.m_v):
                if minimum_weight_edge[nodo] != -1:
                    u = minimum_weight_edge[nodo][0]
                    v = minimum_weight_edge[nodo][1]
                    w = minimum_weight_edge[nodo][2]

                    componente_u = self.m_componente[u]
                    componente_v = self.m_componente[v]
                    operation = operation + 1

                    if componente_u != componente_v:
                        pesoMST += w
                        self.union(sizeComponente, componente_u, componente_v)
                        G.add_edge(u, v, weight=w)
                        print('{0}\t\t{1}\t  {2}'.format(u, v, w).expandtabs(10))
                        numComponents -= 1
                        operation = operation + 1

            minimum_weight_edge = [-1] * self.m_v
            operation = operation + 1
        print("Total weight: " + str(pesoMST))



# Funcion que convierte una lista en entero
# Recibe como argumento una lista
def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return res


start_time = time.time()

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
G = nx.Graph()

content.pop(0)


# Agrego los bordes que hay entre cada nodo
for x in range(len(content)):
    a = content[x][0]
    b = content[x][1]
    c = content[x][2]
    g.agregarArista(a, b, c)
    operation = operation + 1

# Mando a llamar al metodo Boruvka
g.boruvka()

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_size=700)

nx.draw_networkx(G, pos)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0.99, hspace=0.995)

figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

print("Numero de operaciones basicas: ", operation)
print("--- %s seconds ---" % (time.time() - start_time))

plt.show()
