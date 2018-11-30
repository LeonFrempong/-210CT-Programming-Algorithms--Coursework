
import unittest

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
    vertices = {} #vertices is a dictionary, so 
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

class graph(unittest.TestCase):
    self.assertEqual('12', '24')
if __name__ == '__main__':
    unittest.main
