import numpy as np
with open('input.txt') as file:
    lines = file.readlines()
boards = np.array([[l.split() for l in lines[2+i*6:2+i*6+5]] for i in range(int((len(lines)-1)/6))]).astype('int')

def findboards(all_boards, called_numbers):
    winning_indices = (windices:=np.logical_or(np.any(np.all(called := np.isin(all_boards, called_numbers), axis=1), axis=1), np.any(np.all(called, axis=2), axis=1))).nonzero()[0]
    losing_indices = np.logical_not(windices).nonzero()[0]
    return (winning_indices[0] if len(winning_indices) > 0 else -1, losing_indices[0] if len(losing_indices) > 0 else -1)

def uncalled_sum(board, called_numbers):
    return sum((board[np.logical_not(np.isin(board, called_numbers))]).flatten())

nrs = [int(n) for n in lines[0].split(',')]
called_nrs = []
last_winning_index = -2
first_won = False
while last_winning_index != -1:
    (winning_index, losing_index) = findboards(boards, called_nrs)
    if winning_index != -1 and first_won == False:
        first_won = True
        print("first board to win:", winning_index, "| score:", uncalled_sum(boards[winning_index], called_nrs) * called_nrs[-1])
    if losing_index == -1:
        print("last board to win:", last_winning_index, "| score:", uncalled_sum(boards[last_winning_index], called_nrs) * called_nrs[-1])
    last_winning_index = losing_index
    called_nrs.append(nrs.pop(0))