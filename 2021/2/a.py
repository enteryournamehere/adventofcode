with open('input.txt') as file:
    y = 0
    x = 0
    for line in file:
        [command, arg] = line.split()
        arg = int(arg)
        if command == 'forward':
            x += arg
        elif command == 'up':
            y -= arg
        elif command == 'down':
            y += arg
    print(f"x={x}, y={y}, product={x*y}")
