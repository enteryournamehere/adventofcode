with open('input.txt') as file:
    fish = [int(f) for f in file.readline().strip().split(',')]

for day in range(256):
    new_fish = []
    for i in range(len(fish)):
        fish[i] -= 1  # decrease age
        if fish[i] == -1:  # respawn at age 6
            fish[i] = 6
            new_fish.append(8)  # new fish at age 8
    fish += new_fish

print(len(fish))