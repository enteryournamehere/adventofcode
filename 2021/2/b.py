with open('input.txt') as file:
    y = 0
    x = 0
    aim = 0
    for line in file:
        [command, arg] = line.split()
        arg = int(arg)
        if command == 'forward':
            x += arg
            y += arg * aim
        elif command == 'up':
            aim -= arg
        elif command == 'down':
            aim += arg
    print(f"x={x}, y={y}, product={x*y}")
