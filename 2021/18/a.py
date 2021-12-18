a = [[[[4,3],4],4],[7,[[8,4],9]]]
b = [1,1]

import math
import copy

def add(a, b):
    c = [a, b]
    print('addin')
    print(c)
    cccc = []
    while cccc != c:
        cccc = copy.deepcopy(c)
        ccc = []
        while ccc != c:
            ccc = copy.deepcopy(c)
            check_nest(c)

        ccc = []
        while ccc != c:
            ccc = copy.deepcopy(c)
            check_size(c)

    print(c)
    return c

def check_size(current):
    if type(current) is int:
        return False
    if type(current[0]) is int and current[0] >= 10:
        current[0] = [math.floor(current[0] / 2), math.ceil(current[0] / 2)]
        return True
    elif type(current[1]) is int and current[1] >= 10:
        current[1] = [math.floor(current[1] / 2), math.ceil(current[1] / 2)]
        return True
    else:
        a = check_size(current[0])
        if a:
            return True
        b = check_size(current[1])
        if b:
            return True
    return False
    

def check_nest(current, depth = 0):
    to_return = [0, 0]
    if type(current) is not list:
        return to_return

    # left
    if type(current[0]) is list and depth + 1 == 4 and (type(current[0][0]) is int and type(current[0][1]) is int):
        # left el is nested too deep
        # add its right value to our right value
        current[1] = add_to_leftmost_element(current[1], current[0][1])
        # return its left value to our parent
        to_return[0] = current[0][0]
        current[0] = 0
        return to_return
    
    # right
    if type(current[1]) is list and depth + 1 == 4 and (type(current[1][0]) is int and type(current[1][1]) is int):
        # right el is nested too deep :worried:
        # add its left value to our left value
        print('nested too deep:', current[1])
        print('adding to right:', current[1][0])
        current[0] = add_to_rightmost_element(current[0], current[1][0])
        # return its right value to our parent
        to_return[1] = current[1][1]
        current[1] = 0
        return to_return
    
    # not dested yet
    vals = check_nest(current[0], depth + 1)
    if vals[0] != 0 or vals[1] != 0:
        if vals[1] != 0:
            current[1] = add_to_leftmost_element(current[1], vals[1])
            vals[1] = 0
        return vals

    vals = check_nest(current[1], depth + 1)
    if vals[0] != 0 or vals[1] != 0:
        if vals[0] != 0:
            current[0] = add_to_rightmost_element(current[0], vals[0])
            vals[0] = 0
        return vals

    return to_return
    
def magnitude(element):
    if type(element) is int:
        return element
    return 3 * magnitude(element[0]) + 2 * magnitude(element[1])

def add_to_leftmost_element(element, number):
    if type(element) is int:
        return element + number
    else:
        element[0] = add_to_leftmost_element(element[0], number)
        return element

def add_to_rightmost_element(element, number):
    if type(element) is int:
        return element + number
    else:
        element[1] = add_to_leftmost_element(element[1], number)
        return element

add(a, b)

inputs = [
    [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
    [[[5,[2,8]],4],[5,[[9,9],0]]],
    [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
    [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
    [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
    [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
    [[[[5,4],[7,7]],8],[[8,3],8]],
    [[9,3],[[9,9],[6,[4,9]]]],
    [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
    [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
]
total = inputs[0]
for i in range(1, len(inputs)):
    total = add(total, inputs[i])

print(magnitude(total))
# check_nest([[[[[9,8],1],2],3],4], 0)

print(magnitude([[1,2],[[3,4],5]]))