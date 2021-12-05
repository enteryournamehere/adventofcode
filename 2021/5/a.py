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
        for x in range(min(xa, xb), max(xa, xb) + 1):
            point = (x, ya)
            handle_point(point)

    # vertical
    elif xa == xb:
        for y in range(min(ya, yb), max(ya, yb) + 1):
            point = (xa, y)
            handle_point(point)

print(len(overlapping_vent_points))