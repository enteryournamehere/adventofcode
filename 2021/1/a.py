with open('input.txt') as file:
    prev = None
    increased = 0
    while line := file.readline().strip():
        cur = int(line)
        if prev is not None and cur > prev:
            increased += 1
        prev = cur
    print(increased)
