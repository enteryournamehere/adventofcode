class Graph:
    nodes = list()
    adjacency = dict()

    def __init__(self):
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

counter = 0

def search_path(graph: Graph, visited: list, start_node):
    global counter
    visited.append(start_node)

    # small caves
    visited_counts = dict()
    double_visited_small_caves = 0
    for visited_node in set(visited):
        visited_counts[visited_node] = visited.count(visited_node)
    for visited_node in visited_counts:
        if visited_node != visited_node.lower():
            continue
        if visited_counts[visited_node] > 2:  # can't visit a single small cave more than twice
            return 0
        if visited_counts[visited_node] == 2:
            if visited_node == 'start' or visited_node == 'end':  # can't visit start/end more than once
                return 0
            else:
                double_visited_small_caves += 1
        if double_visited_small_caves == 2:  # can't visit more than a single small cave twice
            return 0

    if start_node == 'end':
        return 1

    valid_count = 0
    for other_node in graph.get_adjacent_nodes(start_node):
        counter += 1
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
    print(counter)