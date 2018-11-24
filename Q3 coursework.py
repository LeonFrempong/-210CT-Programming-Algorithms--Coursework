# Undirected, unweighed graph with Adjency Lists
class vertex:
    def __init__(self, n):
        self.name = n
        self.adjacent = list[ ] #adjacent are connected vertices

    def add_adjacent(self, node):
        if node not in self.adjacent:
                    self.adjacent.append(node) 
                    self.adjacent.sort()
        
        
class graph:
    nodes = {}
    #adding  a node (vertex) to the graph
    #checks if vertex passed in is actually a vertex object and doesn't exist in the dictionary yet.
    def add_node(self, node):
        if  (node,Node) and (node.name) not in self.vertices:
            self.vertices[node.name] = node
            return True
        else:
            return False
    #Adding an edge to the graph
    #adding an edge means updating the adjency list of both nodes with the other one
    def add_edge(self, start, end):
        if (start in self.vertices) and  (end in self.vertices):
            self.vertices(start).add_adjacent(end)
            self.vertices(end).add_adjacent(start)  
            return true
        else:
            return false


    #c. Printing the graph.
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].adjacent))

#visualisation 
#g = graph(v,e)
g = graph()
v = node('1')
g.add_node(a)
g.add_node(Node('2'))

for i in range(ord(1))

edge = [ ['1,2'], ['2,4'], ['3,4'], ['3,5'], ['4,5'] ]
