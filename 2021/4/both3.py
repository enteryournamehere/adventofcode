import numpy as np;
lines = open('input.txt').readlines()
boards, nrs, called_nrs, losing_index, winning_score = np.array([[l.split() for l in lines[2+i*6:2+i*6+5]] for i in range(int((len(lines)-1)/6))]).astype('int'), [int(n) for n in lines[0].split(',')], [], -2, -1
while (last_winning_index := losing_index) != -1 and not called_nrs.append(nrs.pop(0)):
    winning_score = sum((boards[winning_index][np.logical_not(np.isin(boards[winning_index], called_nrs))]).flatten()) * called_nrs[-1] if (winning_index := winning_indices[0] if len(winning_indices := (windices:=np.logical_or(np.any(np.all(called := np.isin(boards, called_nrs), axis=1), axis=1), np.any(np.all(called, axis=2), axis=1))).nonzero()[0]) > 0 else -1) != -1 and winning_score == -1 else winning_score
    if (losing_index := losing_indices[0] if len(losing_indices := np.logical_not(windices).nonzero()[0]) > 0 else -1) == -1:
        break
print(winning_score, sum((boards[last_winning_index][np.logical_not(np.isin(boards[last_winning_index], called_nrs))]).flatten()) * called_nrs[-1])
