import numpy as np

letters = """
 ##  #  # #### #  #  ##      #  #  ## 
#  # #### #  # ## # #  #     #  # #  #
#  # #  # #  # ## # #        #  # ##  
#### #  # #  # # ## # ##     #  #   ##
#  # #  # #  # # ## #  #     #  # #  #
#  # #  # #### #  #  ###      ##   ## 
"""

lines = letters.split('\n')[1:-1]
lines = [list(line) for line in lines]
lines = np.array(lines).T

print(lines)
coords = []
for i in range(lines.shape[0]):
    for j in range(lines.shape[1]):
        if lines[i,j] == '#':
            coords.append([i, j])
        pass

num_folds = 10
folds = []
x_max = lines.shape[1]
y_max = lines.shape[0]
for k in range(num_folds):
    axis = 0 if np.random.rand() > 0.5 else 1
    for coord in coords:
        if np.random.rand() > 0.5:
            coord[axis] = [y_max, x_max][axis] + ([y_max, x_max][axis] - coord[axis])

    folds.append('fold along ' + ['x','y'][axis] + '=' + str([y_max, x_max][axis]))

    if axis == 0:
        y_max = y_max * 2 
    else:
        x_max = x_max * 2 

folds.reverse()
print('\n'.join(f'{c[0]},{c[1]}' for c in coords))

lines = [f'{c[0]},{c[1]}' for c in coords]
lines.append('')
lines.extend(folds)

with open('gaming.txt', 'w') as out:
    out.writelines(line + '\n' for line in lines)