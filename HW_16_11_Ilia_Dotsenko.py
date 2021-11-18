# Zadanie domowe 2 (16.11)
# Ilia Dotsenko

class Graph(object):

    def __init__(self, current_dict=None):
        #Graph class constructor
        if current_dict == None:
            current_dict = {}
        self.current_dict = current_dict
        print(self.current_dict)

    def add_node(self, node):
        #Add a node to the graph
        try:
            if node not in self.current_dict:
                self.current_dict[node] = []
                print(self.current_dict)
        except TypeError:
            print('Please provide a non-modifiable object.')    # zamiana wyjątku na komunikat na ekranie nie jest korzystna

    def remove_node(self, node):
        #Remove an existing node with all its edges
        if node in self.current_dict:
            self.current_dict.pop(node)
            for i in self.current_dict: # czy dałoby się to zrobić bardziej wydajnie?
                list1 = self.current_dict[i]
                if node in list1:
                    list1.remove(node)
            print(self.current_dict)

    def add_edge(self, node1, node2):
        #Create an edge between existing node1 and node2
        if node1 in self.current_dict and node2 in self.current_dict:
            self.current_dict[node1].append(node2)
            self.current_dict[node2].append(node1)
            print(self.current_dict)
        else:
            print('An edge can be created only between existing nodes.')    # raise ValueError

    def remove_edge(self, node1, node2):
        #Remove edge between connected node1 and node2
        if node1 in self.current_dict:
            if node2 in self.current_dict:
                if node2 in self.current_dict[node1]:
                    self.current_dict[node1].remove(node2)
                    self.current_dict[node2].remove(node1)
                    print(self.current_dict)
                else:
                    print(node1, ' is not connected to ', node2)
            else:
                print(node2, ' does not exist')
        else:
            print(node1, ' does not exist')

    def get_neighbors(self, node):
        #Get neighboring nodes of the given node
        k = 0
        neighbors = []
        if node in self.current_dict:
            for i in self.current_dict: # czy to na pewno jest wydajny sposób zwrócenia wszystkich sąsiadów?
                list1 = self.current_dict[i]
                if node in list1:
                    neighbors.append(i)
                    k += 1
            if k==0:    # po co to? lepiej zwrócić pustą listę niż None; a jeśli już, to len(neighbors)
                return None
            else:
                return neighbors

    visited_nodes = []  # absolutnie zły pomysł - wszystkie grafy mają jedną wspólną listę; zresztą wystarczy spróbować przeiterować dwa razy po jednym grafie
    queued_nodes = []

    def bfs(self, node):
        #Breadth-first search starting from the given node
        self.visited_nodes.append(node)
        self.queued_nodes.append(node)
        while self.queued_nodes:
            s = self.queued_nodes.pop(0)

            for neighbor in self.get_neighbors(s):
                if neighbor not in self.visited_nodes:
                    self.visited_nodes.append(neighbor)
                    self.queued_nodes.append(neighbor)
        return iter(self.visited_nodes)

    def dfs(self, node, visited_nodes=[]):
        #Depth-first search starting from the given node
        if node not in visited_nodes:
            visited_nodes.append(node)
            for neighbor in self.get_neighbors(node):
                self.dfs(neighbor, visited_nodes)
        return iter(visited_nodes)


print('Creating an object of class Graph graph1: ')
graph1 = Graph(current_dict={'a': ['b', 'c'],
                             'b': ['c','a', 'f'],
                             'f': ['b', 'g', 'z', 'd'],
                             'z': ['f'],
                             'g': ['f'],
                             'c': ['a', 'd', 'b'],
                             'd': ['c', 'f']})

print('Adding a node e: ')
graph1.add_node('e')

print('Adding an edge between e and f: ')
graph1.add_edge('e','f')

print('Listing neghbors of f and c nodes.')
print(graph1.get_neighbors('f'))
print(graph1.get_neighbors('c'))

print('Removing node e: ')
graph1.remove_node('e')

print('Removing edge between nodes f and d: ')
graph1.remove_edge('f', 'd')

print('Returning depth-first search results for node b ')
for i in graph1.dfs('b'):
    print(i, end=' ')

for j in range(4):    
    print('\nReturning breadth-first search results for node b ')
    for i in graph1.bfs('b'):
        print(i, end=' ')
