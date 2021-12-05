vent_points = set()
overlapping_vent_points = set()

def handle_point(point):
    if point in vent_points and point not in overlapping_vent_points:
        overlapping_vent_points.add(point)
    vent_points.add(point)

for line in open('input.txt'):
    spl = line.split(' -> ')
    a = tuple(map(int, spl[0].split(',')))
    b = tuple(map(int, spl[1].split(',')))
    xa, ya = a
    xb, yb = b

    # horizontal
    if ya == yb:
        range_x = range(min(xa, xb), max(xa, xb) + 1)
        range_y = [ya] * len(range_x)

    # vertical
    elif xa == xb:
        range_y = range(min(ya, yb), max(ya, yb) + 1)
        range_x = [xa] * len(range_y)

    # diagonal
    else:
        difference = yb - ya
        difference_y = yb - ya
        difference_x = xb - xa
        step_y = 1 if difference_y > 0 else -1
        step_x = 1 if difference_x > 0 else -1
        range_x = range(xa, xa + difference_x + step_x, step_x)
        range_y = range(ya, ya + difference_y + step_y, step_y)

    for i in range(len(range_x)):
        point = (range_x[i], range_y[i])
        handle_point(point)

print(len(overlapping_vent_points))