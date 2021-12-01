import numpy as np
print(sum((m:=np.loadtxt('input.txt'))[3:]-m[:-3]>0))
