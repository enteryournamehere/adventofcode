with open('input.txt') as file:
    fish = [int(f) for f in file.readline().strip().split(',')]

fish_by_age = [0] * 9  # age 0 - 8

for fishy in fish:
    fish_by_age[fishy] += 1  # count fish per age

for day in range(256):
    resetting_fish = new_fish = fish_by_age[0]  # amount of fish to spawn at age 6 and 8
    for age in range(1, len(fish_by_age)):
        fish_by_age[age - 1] = fish_by_age[age]  # decrease age
    fish_by_age[8] = new_fish  # new fish
    fish_by_age[6] += resetting_fish  # respawning fish

print(sum(fish_by_age))