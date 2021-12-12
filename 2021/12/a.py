class Graph:
    nodes = list()
    adjacency = dict()

    def __init__(self):
        # self.nodes = list
        pass

    def get_adjacent_nodes(self, node):
        return self.adjacency[node]

    def add_node(self, node):
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.adjacency[node] = list()

    def set_adjacent(self, node_a, node_b):
        self.adjacency[node_a].append(node_b)
        self.adjacency[node_b].append(node_a)
        # yeah could be more efficient ok
    
    def __str__(self):
        return str(self.adjacency)
    
def search_path(graph: Graph, visited: list, start_node):
    visited.append(start_node)

    # small caves
    if visited.count(start_node) == 2 and start_node == start_node.lower():
        return 0

    print(start_node)

    if start_node == 'end':
        print("-----------", visited)
        return 1

    valid_count = 0
    for other_node in graph.get_adjacent_nodes(start_node):
        print(f"{start_node}: checking {other_node}, visited: {visited}")
        found = search_path(graph, visited, other_node)
        visited.pop()
        if found:
            valid_count += found
    
    return valid_count

with open('input.txt') as file:
    graph = Graph()
    while line := file.readline().strip():
        start, end = line.split('-')
        graph.add_node(start)
        graph.add_node(end)
        graph.set_adjacent(start, end)
    print(graph)
    a = search_path(graph, [], 'start')
    print(a)