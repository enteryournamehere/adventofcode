with open('input.txt') as file:
    origins = list(map(int, file.readline().split(',')))

min_fuel = 1e20
for target in range(min(origins), max(origins) + 1):
    fuel_used = 0
    for origin in origins:
        fuel_used += abs(target - origin)
    if fuel_used < min_fuel:
        min_fuel = fuel_used

print(min_fuel)