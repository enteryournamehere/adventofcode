import numpy as np
data = np.array([(list(line.strip())) for line in open('input.txt').readlines()]).astype('int')
data = np.pad(data, [(1,1), (1,1)], constant_values=10)

lower_than_left   = (data[:,1:]  - data[:,:-1])[1:-1,:-1] < 0
lower_than_right  = (data[:,:-1] - data[:,1:])[1:-1,1:] < 0
lower_than_top    = (data[1:,:]  - data[:-1])[:-1,1:-1] < 0
lower_than_bottom = (data[:-1,]  - data[1:,:])[1:,1:-1] < 0

low_points = np.all([lower_than_left, lower_than_right, lower_than_top, lower_than_bottom], axis=0)

risk_levels = low_points + low_points * data[1:-1,1:-1]

print(np.sum(risk_levels))