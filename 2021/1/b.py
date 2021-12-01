with open('input.txt') as file:
    prev_4 = []
    increased = 0
    while line := file.readline().strip():
        cur = int(line)
        prev_4.append(cur)
        if len(prev_4) > 4:
            prev_4.pop(0)
        if len(prev_4) < 4:
            continue
        sum_1 = sum(prev_4[:-1])
        sum_2 = sum(prev_4[1:])
        if sum_2 > sum_1:
            increased += 1
    print(increased)
