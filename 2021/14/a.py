rules = []
steps = 40

template = str()

with open('input.txt') as file:
    template = list(file.readline().strip())
    file.readline()

    while line := file.readline().strip():
        rules.append(line.split(' -> '))

    print(template)
    print(rules)
    print()

for step in range(steps):
    i = 0
    print(f'step {step}, template length {len(template)}')
    while i < len(template) - 1:
        for rule in rules:
            if rule[0] == template[i] + template[i+1]:
                # print(f'match at i={i} : {rule[0]}, total {"".join(template)}')
                template.insert(i+1, rule[1])
                i += 1
                break
        i += 1

counts = dict()
for char in template:
    counts[char] = counts.get(char, 0) + 1
print(max(counts.values()) - min(counts.values()))
# print(counts)
# print("".join(template))