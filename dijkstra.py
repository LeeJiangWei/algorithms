class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.E = []  # store all the edges and weights
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]


    #generate edges set using graph
    def generateEdges(self):
        for i in range(self.V):
            for j in range(i, self.V):
                if self.graph[i][j] != 0:
                    self.E.append([i, j, g.graph[i][j]])

    def minDistance(self, dist, sptSet):
        #use 9999 to represent infinite number
        min = 9999
        min_index = 0

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index


    def DijkstraSP(self, src):

        dist = [9999 for v in range(self.V)]
        dist[src] = 0
        sptSet = [False for v in range(self.V)]

        for i in range(self.V):

            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        print("Vertex Distance from Source:")
        for node in range(self.V):
            print("vertex:", node + 1, " distance:", dist[node])



g= Graph(7)
g.graph = [[0,5,7,12,0,0,0],
           [0,0,1,0,6,0,0],
           [0,0,0,1,5,10,0],
           [0,0,0,0,0,13,0],
           [0,0,0,0,0,2,7],
           [0,0,0,0,0,0,3],
           [0,0,0,0,0,0,0]]

g.DijkstraSP(0)