import sys


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        count = 0
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
            count = count + self.graph[i][parent[i]]

        print("Total weight: " + str(count))

    def minKey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):

                if 0 < self.graph[u][v] < key[v] and mstSet[v] == False:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return res


filename = sys.argv[-1]
file = open(filename)

with open(filename) as f:
    content = [[int(j) for j in line.split(',')] for line in f if line.strip() != ""]
file.close()

num = convert(content[0])
g = Graph(num)
content.pop(0)

g.graph = content

g.primMST()
