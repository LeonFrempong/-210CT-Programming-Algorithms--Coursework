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
    #checks if vertex passed in is actually a vertex object and doesn't exist in the dictionary yet.
    def add_node(self, node):
        if  (node,Vertex) and (node.name) not in self.vertices:
            self.vertices[node.name] = node
            return True
        else:
            return False
        
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

    def Depth_first_search(g, start):
        newStack= [] 
        visited = []
        s.push(start) # vertex in to the list
        while s != empty: 
            end = s.pop() #vertex(node) out of the list
            if end not in visited:
                visited.append(end)#add vertex at the end of the node to be visited
                for all edges, e, in end, s.push(e.to):
        return (visited)

    def BREADTH_FIRST_SEARCH(g, start):
        newQueue =() 
        visited=[]
        Q.enqueue(start)
        while Q != empty: 
            end = q.dequeue()
            if end not in visited:
                visited.append(end) # moves to the next vertex
            for all edges, e, from end:# iterates through edges
                Q.enqueue(e.to)
        return (visited)
"""
Title: path function
#Author: Edd Mann
#Date: 30/11/2018
#Availability: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
"""
      
    def isPath(g, start, end, path=None):
        if path == None:
           path = [start]
        if start == end:
           return path
    
#open file and write file
    adjacency_list = open("graph_file", "w")
    print (adjacency_list)

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
BREADTH_FIRST_SEARCH(g, start)
Depth_first_search(g, start)
