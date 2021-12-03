import numpy as np
data = np.loadtxt('input.txt', dtype='str')
totals = None
for dat in data:
    separate = np.array(list(dat)).astype('int')
    totals = totals + separate if totals is not None else separate
majority = totals > len(data) / 2
gamma = int(''.join(majority.astype('int').astype('str')), 2)
epsilon = int(''.join((1 - majority.astype('int')).astype('str')), 2)
print(gamma, epsilon, gamma * epsilon)
