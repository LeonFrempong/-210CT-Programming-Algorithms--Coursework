edges = ['12', '24', '34', '35', '45']

# Undirected, unweighed graph with Adjency Lists
class Vertex:
    def __init__(self, n):
        self.name = n
        self.adjacent = list() #adjacent are connected vertices

    def add_adjacent(self, node):
        if node not in self.adjacent:
                    self.adjacent.append(node) 
                    self.adjacent.sort()
        
        
class graph:
    vertices = {} #vertices is a dtionary, so 
    #adding  a node (vertex) to the graph
    #checks if vertex passed in is actually a vertex object and doesn't exist in the dictionary yet.
    def add_node(self, node):
        if  (node,Vertex) and (node.name) not in self.vertices:
            self.vertices[node.name] = node
            return True
        else:
            return False
    #Adding an edge to the graph
    #adding an edge means updating the adjency list of both nodes with the other one
    def add_edge(self, start, end):
        if start in self.vertices and end in self.vertices:
            self.vertices[start].add_adjacent(end)
            self.vertices[end].add_adjacent(start)  
            return True
        else:
            return False


    #c. Printing the graph.
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].adjacent))

    #this function checks whether the graph is strongly connected or not

    def isPath(self, start, end, path=None):
        if path == None:
            path[]
        graph = self. __graph_dict
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
        





    def isConnected(g, start, end, nPath = []):
        if Vertex == Vertex:
            return nPath
            print("yes")
        else:
            print("No")
"""           

#BFS() function

def BREADTH_FIRST_SEARCH(G,v):
    Q = new Queue()
    visited = []
    Q.enqueue(V)
    while Q is not empty:
        u = q.dequeue()
        if u is not in visited:
            visited.append(u)
        for all edges, e, from u:
            Q.enqueue(e.to)
    return visited 
        



#DFS (Depth First Search)function

def DEPTH_FIRST_SEARCH(G, v):
    S = new Stack()
    visited = []
    S.push(v)
    while S is not empty:
        u = S.pop()
        if u is not in visited:
            visited.append(u)
            for all adges, e, from u, S.push(e.to)
    return visited
"""
            #visualisation 
#g = graph(v,e)
g = graph()
a = Vertex('0')
g.add_node(a)
g.add_node(Vertex('1'))

for i in range(ord('0'), ord('6')): #it iterates the nodes in the graph
    g.add_node(Vertex(chr(i)))

for edge in edges:
    g.add_edge(edge[:1], edge[1:])
g.print_graph()
isConnected()
