import numpy as np

img = []
outer_value = False

complete_dark_index = 0
complete_light_index = int('111111111', 2)

def get_cell_value(x, y):
    if x < 0 or y < 0 or x >= img.shape[0] or y >= img.shape[1]:
        return outer_value
    return img[x, y]

with open('input.txt') as file:
    enhancer = np.array(list(file.readline().strip())) == '#'
    file.readline()
    while line := file.readline().strip():
        img.append(np.array(list(line)) == '#')

img = np.array(img)

for line in img:
    print(''.join(['.', '#'][int(d)] for d in line))
print()

for i in range(2):
    points_that_might_change_plus_border = np.pad(img, 2, mode='constant', constant_values=outer_value)
    output = np.zeros(points_that_might_change_plus_border.shape)
    
    for x in range(1, points_that_might_change_plus_border.shape[0] - 1):
        for y in range(1, points_that_might_change_plus_border.shape[1] - 1):
            data = points_that_might_change_plus_border[x-1:x+2,y-1:y+2]
            binary = ''.join(['0', '1'][int(d)] for d in data.flatten())
            index = int(binary, 2)
            output[x, y] = enhancer[index]
            img = output[1:-1, 1:-1] # trim edge

    outer_value = enhancer[complete_light_index] if outer_value else enhancer[complete_dark_index]

for line in img:
    print(''.join(['.', '#'][int(d)] for d in line))
print()

print(int(np.sum(img)))

