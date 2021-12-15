from os import path
import numpy as np
lines = open('input.txt').readlines()
chars = [list(line.strip()) for line in lines]
bep = np.array(chars).astype(int)

BIG = 1e10

# create big map
first_row = [bep + i for i in range(5)]
first_row_merged = np.concatenate(first_row, axis=1)
rows = [first_row_merged + i for i in range(5)]
bep = (np.concatenate(rows, axis=0) - 1) % 9 + 1

# initialize distance matrix
shortest_path_to = np.full(bep.shape, BIG)
shortest_path_to[0, 0] = 0

def calculate_shortest_path_length():
    for x in range(bep.shape[0]):
        for y in range(bep.shape[0]):
            # find out what the shortest path length is when
            # arriving from one of the 4 neighbours
            # and remember it in shortest_path_to
            shortest_path_to[x, y] = min(
                shortest_path_to[x, y],
                shortest_path_to[x+1, y] + bep[x, y] if x+1 < bep.shape[0] else BIG,
                shortest_path_to[x-1, y] + bep[x, y] if x-1 >= 0 else BIG,
                shortest_path_to[x, y+1] + bep[x, y] if y+1 < bep.shape[1] else BIG,
                shortest_path_to[x, y-1] + bep[x, y] if y-1 >= 0 else BIG
            )
    return shortest_path_to[-1,-1]

prev_iteration_path_length = BIG

while True:
    path_length = calculate_shortest_path_length()
    print(path_length)
    if path_length == prev_iteration_path_length:
        break
    prev_iteration_path_length = path_length

# yes it should probably run until no path lengths change anymore but this works
path_length = calculate_shortest_path_length()

print(path_length)