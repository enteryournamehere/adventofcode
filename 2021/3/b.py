import numpy as np
data = np.loadtxt('input.txt', dtype='str')
data = np.array([list(a) for a in data]).astype('int')

def find_thing(array, inverted=False):
    checking_bit = 0
    while len(array) > 1:  # search until 1 number is left
        bit_value = (np.mean(array, axis=0) >= 0.5)[checking_bit]  # get average of each column, check where >= 0.5, look at current bit index
        if inverted:  # switch to least common bit instead
            bit_value = 1 - bit_value
        array = array[array[:,checking_bit] == bit_value]  # filter array
        checking_bit += 1  # look at next bit
    return int(''.join(array[0].astype('str')),2)

oxy = find_thing(data)
co2 = find_thing(data, True)
print(oxy, co2, oxy * co2)
