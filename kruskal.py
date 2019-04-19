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

    def addEdge(self, u, v, w):
        self.E.append([u, v, w])


    # find set
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])


    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # path compression make the low tree
        # as children of the root node of high tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    def KruskalMST(self):

        result = []

        i = 0  # used for sorting edges
        e = 0  # used for counting edges of a tree

        # sort all edges by weights(item[2])
        # in incresing order(default)
        self.E = sorted(self.E, key=lambda item: item[2])

        parent = [];
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.E[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        for i in range(len(result)):
            result[i][0] += 1
            result[i][1] += 1

        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d -- %d weight: %d" % (u, v, weight))


    def minDistance(self, dist, sptSet):
        #use 9999 to represent infinite number
        min = 9999
        min_index = 0

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index


g = Graph(6)
# g.addEdge(0, 1, 3)
# g.addEdge(0, 2, 2)
# g.addEdge(0, 5, 10)
# g.addEdge(1, 2, 2)
# g.addEdge(1, 3, 4)
# g.addEdge(1, 4, 4)
# g.addEdge(2, 3, 9)
# g.addEdge(2, 4, 5)
# g.addEdge(2, 5, 3)
# g.addEdge(3, 4, 6)
# g.addEdge(4, 5, 7)
g.graph=[[0,3,2,0,0,10],
         [3,0,2,4,4,0],
         [2,2,0,9,5,3],
         [0,4,9,0,6,0],
         [0,4,5,6,0,7],
         [10,0,3,0,7,0]]
g.generateEdges()
g.KruskalMST()