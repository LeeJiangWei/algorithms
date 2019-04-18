class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.E = []  # store all the edges and weights
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]


    def minDistance(self, dist, sptSet):
        #use 9999 to represent infinite number
        min = 9999
        min_index = 0

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index


    def PrimMST(self, src):

        dist = [9999 for v in range(self.V)]
        dist[src] = 0
        mstSet = [False for v in range(self.V)]
        parent=[None for v in range(self.V)]

        for i in range(self.V):

            u = self.minDistance(dist, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and \
                        dist[v] > self.graph[u][v]:
                    dist[v] = self.graph[u][v]
                    parent[v] = u
            #print("\nmst:",mstSet,"\ndist:",dist,"\nparent:",parent)


        print("Following are the edges in the constructed MST")
        for i in range(1, self.V):
            print("%d -- %d weight:%d" %(parent[i]+1, i+1, self.graph[i][parent[i]]))

g = Graph(6)

g.graph=[[0,3,2,0,0,10],
         [3,0,2,4,4,0],
         [2,2,0,9,5,3],
         [0,4,9,0,6,0],
         [0,4,5,6,0,7],
         [10,0,3,0,7,0]]

g.PrimMST(0)