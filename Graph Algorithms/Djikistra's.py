
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(len(vertices))]
                      for row in range(len(vertices))]

    def findMinDist(self, dist, sptset):
        minDist = 10e7
        min_dist_index = 0
        for i in range(len(dist)):
            if not sptset[i] and i<= minDist:
                minDist = dist[i]
                min_dist_index = i
        return min_dist_index

    def dijikstra(self, source):
        max_dist = 10e7
        dist = [max_dist]*len(self.V)
        dist[source] = 0
        sptset = [False]*len(self.V)

        for _ in range(len(self.V)):
            u = self.findMinDist(dist, sptset)
            sptset[u] = True
            for v in range(len(self.V)):
                if not sptset[v] and (dist[v] > (dist[u] + self.V[u][v])) and self.V[u][v] > 0:
                    dist[v] = dist[u] + self.V[u][v]

        return dist


G = Graph([[0,2,0,0,0,10],
          [2,0,3,0,0,0],
           [0,3,0,5,0,0],
           [0,0,5,0,1,7],
           [0,0,0,1,0,6],
           [10,0,0,7,6,0]])
print(G.dijikstra(0))
