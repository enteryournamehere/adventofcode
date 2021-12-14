import copy

rules = []  # [AB, C]
steps = 40

template = str()

with open('input.txt') as file:
    template = str(file.readline().strip())
    file.readline()

    while line := file.readline().strip():
        rules.append(line.split(' -> '))

# set up pairs dict, containing info about counts and pair rules
pairs = dict()

for rule in rules:
    pairs[rule[0]] = {
        'creates': [rule[0][0] + rule[1], rule[1] + rule[0][1]],
        'inserted_letter': rule[1],
        'count': 0
    }

# count initial pairs
for i in range(len(template) - 1):
    pairs[template[i:i+2]]['count'] += 1

# letter counts
counts = dict()

for char in template:
    counts[char] = counts.get(char, 0) + 1

for step in range(steps):
    # copy so we don't look at newly created pairs in this iteration
    pairs_new = copy.deepcopy(pairs)

    for pair, pair_info in pairs.items():
        creates = pair_info['creates']
        pairs_new[creates[0]]['count'] += pair_info['count']
        pairs_new[creates[1]]['count'] += pair_info['count']
        counts[pair_info['inserted_letter']] = counts.get(pair_info['inserted_letter'], 0) + pair_info['count']
        pairs_new[pair]['count'] -= pair_info['count']
    pairs = pairs_new

print(max(counts.values()) - min(counts.values()))
