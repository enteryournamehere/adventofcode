import numpy as np
print(sum((m:=np.loadtxt('input.txt'))[1:]-m[:-1]>0))
