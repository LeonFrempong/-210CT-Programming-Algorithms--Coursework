# Undirected, unweighed graph with Adjency Lists
class vertex:
    def __init__(self, n):
        self.name = n
        self.adjacent = list() #adjacent are connected vertices

    def add_adjacent(self, node):
        if node not in self.adjacent:
                    self.adjacent.append(node) 
                    self.adjacent.sort()
        
        
class graph:
    nodes = {}
    #adding  a node (vertex)
    #checks if vertex passed in is actually a vertex object and doesn't exist in the dictionary yet.
    def add_node(self, node):
        if  (node,Node) and (node.name) not in self.vertices:
            self.vertices[node.name] = node
            return True
        else:
            return False
    #adding an edge means updating the adjency list of both nodes with the other one
    def add_edge(self, )

    #a. Adding a node to the graph.
    #b. Adding an edge to the graph.
    #c. Printing the graph.


#visualisation 
g = graph(v,e)
v = vertex('1')


edges = [ ['12'], ['24'], ['34'], ['35'], ['45'] ]
