import numpy as np
energies = np.array([(list(line.strip())) for line in open('input.txt').readlines()]).astype('int')

def flash(energies, has_flashed, x, y):
    # check energy level
    if energies[x][y] <= 9:
        return 0
    
    # only flash once per step
    if has_flashed[x][y]:
        return 0
    
    # remember
    has_flashed[x][y] = True

    # number of flashes caused by this octopus
    count = 1

    # try flashing adjacent octopi
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            newx = x + dx
            newy = y + dy
            # stay in bounds
            if newx < 0 or newy < 0 or newx >= energies.shape[0] or newy >= energies.shape[1]:
                continue
            # increase their energy (caused by current octopus's flash)
            energies[newx][newy] += 1
            # let them flash
            count += flash(energies, has_flashed, newx, newy)

    return count

def step(energies):
    flashes = 0
    # increase all energy levels
    energies += 1

    # initialize to 0
    has_flashed = np.zeros(energies.shape).astype(bool)

    # let all octopi with sufficient energy flash
    for x in range(energies.shape[0]):
        for y in range(energies.shape[1]):
            flashes += flash(energies, has_flashed, x, y)

    # reset energy of those who have flashed to 0
    energies[np.where(has_flashed)] = 0
    return flashes

total_flashes = 0
super_flash_found = False
i = 1
while i <= 100 or not super_flash_found:
    flash_count = step(energies)
    total_flashes += flash_count

    if flash_count == np.size(energies):
        print("first synchronized flash at step", i)
        super_flash_found = True
        
    if i == 100:
        print("total flashes after 100 steps:", total_flashes)

    i += 1
