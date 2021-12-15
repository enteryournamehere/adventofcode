import numpy as np
lines = open('input.txt').readlines()
chars = [list(line.strip()) for line in lines]
bep = np.array(chars).astype(int)

BIG = 1e10

shortest_path_to = np.full(bep.shape, BIG)
shortest_path_to[0, 0] = 0

def calculate_shortest_path_length():
    for x in range(bep.shape[0]):
        for y in range(bep.shape[0]):
            shortest_path_to[x, y] = min(
                shortest_path_to[x, y],
                shortest_path_to[x+1, y] + bep[x, y] if x+1 < bep.shape[0] else BIG,
                shortest_path_to[x-1, y] + bep[x, y] if x-1 >= 0 else BIG,
                shortest_path_to[x, y+1] + bep[x, y] if y+1 < bep.shape[1] else BIG,
                shortest_path_to[x, y-1] + bep[x, y] if y-1 >= 0 else BIG
            )
    return shortest_path_to[-1,-1]

shortest_path_to_end = BIG
while calculate_shortest_path_length() != shortest_path_to_end:
    shortest_path_to_end = calculate_shortest_path_length()
    
print(shortest_path_to_end)