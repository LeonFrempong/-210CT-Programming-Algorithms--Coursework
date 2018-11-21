# Undirected, unweighed graph with Adjency Lists
class vertex:
    def __init__(self, n):
        self.name = n
        self.adjacent = list()

    def add_adjacent(self, node):
        if node not in self.adjacent:
                    self.adjacent.append(node)
                    self.adjacent.sort()
        
        


class graph:
    #adding  a node
    #adding an edge means updating the adjency loist of both nodes with the other one


    #a. Adding a node to the graph.
    #b. Adding an edge to the graph.
    #c. Printing the graph.


#visualisation 
g = graph(v,e)
v = vertex('1')


edges = [ ['12'], ['24'], ['34'], ['35'], ['45'] ]
