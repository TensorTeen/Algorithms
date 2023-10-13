from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
count = []


class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def addEdge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex, l):
        visited_vertex[d] = True
        l.append(d)
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex, l)
        return l

    def fillOrder(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fillOrder(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def print_scc(self):
        global count
        stack = []
        visited_vertex = [False] * self.V
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fillOrder(i, visited_vertex, stack)

        gr = self.transpose()
        visited_vertex = [False] * self.V
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                new = [0,]
                cou = gr.dfs(i, visited_vertex, new)
                count.append(cou)

    def getEdgesFromFile(self, path):
        with open(path, 'r') as f:
            for i in f:
                edge = [int(x) for x in i.split()]
                self.addEdge(*edge)


graph = Graph(875715)
graph.getEdgesFromFile(r"E:\Workspace\SCC.txt")
graph.print_scc()
count2 = []
for i in count:
    count2.append(len(i))
print(sorted(count2))