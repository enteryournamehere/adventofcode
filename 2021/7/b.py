with open('input.txt') as file:
    origins = list(map(int, file.readline().split(',')))

# yeah this can be optimized a bunch
min_fuel = 1e20
for target in range(min(origins), max(origins) + 1):
    fuel_used = 0
    for origin in origins:
        fuel_used += sum(range(abs(target - origin) + 1))
    if fuel_used < min_fuel:
        min_fuel = fuel_used

print(min_fuel)