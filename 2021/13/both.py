import numpy as np

def main():
    data = []
    folds = []
    with open('input.txt') as file:
        for line in file:
            if ',' in line:
                data.append([int(c) for c in line.split(',')])
            elif 'fold' in line:
                spl = line.split('=')
                spl2 = spl[0].split(' ')
                folds.append({
                    'axis': spl2[-1],
                    'coordinate': int(spl[1]),
                })
        data = np.array(data)
        print(f'Start shape: {np.max(data, axis=0)}')
        # print(f'Distinct points: {count_distinct(data)}')
    
    for fold_instruction in folds:
        print(f'Folding along {fold_instruction["axis"]}={fold_instruction["coordinate"]}...')
        fold(data, fold_instruction['axis'], fold_instruction['coordinate'])
        # print(f'Distinct points remaining: {count_distinct(data)}')
    
    print_data(data)

def fold(data, axis, coordinate):
    """fold array in-place"""
    axis_index = 1 if axis == 'y' else 0
    for point in data:
        point[axis_index] = min(point[axis_index], coordinate - abs(point[axis_index] - coordinate))

def count_distinct(data):
    """count number of visible points in data"""
    distinct = []
    for point in data:
        ls = list(point)
        if ls in distinct:
            continue
        distinct.append(ls)
    return len(distinct)

def print_data(data):
    [x_max, y_max] = np.max(data, axis=0)
    print(f'End shape: {[x_max, y_max]}')
    # initialize 2d array with spaces
    grid = np.full(shape=(x_max + 1, y_max + 1), fill_value=' ')
    # draw points
    for point in data:
        grid[point[0]][point[1]] = '#'
    # transpose so the letters are oriented correctly
    grid = grid.T
    print()
    for line in grid:
        print(''.join(line))

if __name__ == '__main__':
    main()