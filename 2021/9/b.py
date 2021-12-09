import numpy as np
data = np.array([(list(line.strip())) for line in open('input.txt').readlines()]).astype('int')
padded_data = np.pad(data, [(1,1), (1,1)], constant_values=10)

lower_than_left = (padded_data[:,1:] - padded_data[:,:-1])[1:-1,:-1] < 0
lower_than_right = (padded_data[:,:-1] - padded_data[:,1:])[1:-1,1:] < 0
lower_than_top = (padded_data[1:,:] - padded_data[:-1])[:-1,1:-1] < 0
lower_than_bottom = (padded_data[:-1,] - padded_data[1:,:])[1:,1:-1] < 0

low_points = np.all([lower_than_left, lower_than_right, lower_than_top, lower_than_bottom], axis=0)

def visit(x, y):
    # return if going outside boundaries
    if x < 0 or y < 0 or x >= data.shape[0] or y >= data.shape[1]:
        return 0

    # already visited, or basin edge
    if data[x][y] >= 9:
        return 0

    # set point as visited
    data[x][y] = 9

    # recursion !
    return 1 + visit(x-1, y) \
     + visit(x+1, y) \
     + visit(x, y-1) \
     + visit(x, y+1)

sizes = []

# find size of each basin
for coords in np.argwhere(low_points):
    size = visit(coords[0], coords[1])
    sizes.append(size)

sizes.sort()
print(sizes[-3] * sizes[-2] * sizes[-1])
