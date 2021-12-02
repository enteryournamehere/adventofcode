import numpy as np
cmds = np.loadtxt('input.txt', dtype='str', usecols=0)
args = np.loadtxt('input.txt', dtype='int', usecols=1)
x = sum(args[cmds == 'forward'])
y = sum(args[cmds == 'down']) - sum(args[cmds == 'up'])
print(f"x={x}, y={y}, product={x*y}")
