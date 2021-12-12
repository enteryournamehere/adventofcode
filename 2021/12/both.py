PART = "b"
INPUT_FILE = "input.txt"

def main():
    if PART not in ["a", "b"]:
        return
        
    with open(INPUT_FILE) as file: 
        graph = Graph()
        while line := file.readline().strip():
            start, end = line.split('-')
            graph.add_node(start)
            graph.add_node(end)
            graph.set_adjacent(start, end)
        path_count = find_paths(graph, Path([]), 'start')
        print(f'Distinct valid paths: {path_count}')

class Path(list):
    doubled_node = ['', 0]

    def __init__(self, nodes):
        self.extend(nodes)

class Graph:
    nodes = list()
    adjacency = dict()

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

# depth first search
def find_paths(graph: Graph, visited: list, start_node: str):
    visited.append(start_node)

    # small caves
    if PART == "a" and not valid_path_a(visited, start_node) \
        or PART == "b" and not valid_path_b(visited, start_node):
        return 0

    if start_node == 'end':
        # print(visited)
        return 1

    valid_count = 0
    for other_node in graph.get_adjacent_nodes(start_node):
        found = find_paths(graph, visited, other_node)
        removed = visited.pop()
        # decrease the number of times we visited this node because we removed it from the path
        if visited.doubled_node[0] == removed:
            visited.doubled_node[1] -= 1
            # no longer a duplicate node
            if visited.doubled_node[1] == 1:
                visited.doubled_node = ['', 0]
        if found:
            valid_count += found
    
    return valid_count

def valid_path_a(path, newest_node):
    return path.count(newest_node) != 2 if newest_node.lower() == newest_node else True

def valid_path_b(path, newest_node):
    # large caves can be visited without limitations
    if newest_node == newest_node.upper():
        return True
    # visit start node only once
    if len(path) > 1 and newest_node == 'start':
        return False
    # if this node is already twice in the path, we can't visit it again
    if path.doubled_node[0] == newest_node:
        path.doubled_node[1] += 1
        return False
    # if another node has already been visited twice, and we're about to visit this one for the 2nd time, we can't
    elif path.count(newest_node) == 2:
        if path.doubled_node[1] == 2:
            return False
        # remember that we visited this node twice
        path.doubled_node = [newest_node, 2]
    return True

if __name__ == '__main__':
    main()