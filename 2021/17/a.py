import re
data = open('input.txt').read()
beep = re.findall('-?\d+', data)
coords = [int(c) for c in beep]
xlim, ylim = coords[:2], coords[2:]

def sim(init):
    x, y = 0, 0
    vx, vy = init
    highest_y = 0
    while True:
        x += vx
        y += vy
        vx = vx - 1 if vx > 0 else 0  # does not handle negative x speeds
        vy = vy - 1
        highest_y = max(highest_y, y)
        if is_inside((x, y), xlim, ylim):
            return highest_y
        if x > xlim[1] or y < ylim[0]:
            return None

def is_inside(point, xlim, ylim):
    return point[1] >= ylim[0] and point[1] <= ylim[1]

top = 0

for vy in range(ylim[0], -ylim[0] + 1):
    sam = sim((0, vy))
    if sam:
        top = sam

print(top)