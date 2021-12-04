import numpy as np
lines = open('input.txt').readlines()
boards = np.array([[l.split() for l in lines[2+i*6:2+i*6+5]] for i in range(int((len(lines)-1)/6))]).astype('int')
def findboards():
    winning_indices, losing_indices = (windices:=np.logical_or(np.any(np.all(called := np.isin(boards, called_nrs), axis=1), axis=1), np.any(np.all(called, axis=2), axis=1))).nonzero()[0], np.logical_not(windices).nonzero()[0]
    return (winning_indices[0] if len(winning_indices) > 0 else -1, losing_indices[0] if len(losing_indices) > 0 else -1)
def score(index):
    return sum((boards[index][np.logical_not(np.isin(boards[index], called_nrs))]).flatten()) * called_nrs[-1]
nrs, called_nrs, losing_index, winning_score = [int(n) for n in lines[0].split(',')], [], -2, -1
while (last_winning_index := losing_index) != -1:
    (winning_index, losing_index) = findboards()
    if winning_index != -1 and winning_score == -1:
        winning_score = score(winning_index)
    if losing_index == -1:
        break
    called_nrs.append(nrs.pop(0))
print(winning_score, score(last_winning_index))