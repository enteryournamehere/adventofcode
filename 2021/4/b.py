import numpy as np

with open('input.txt') as file:
    lines = file.readlines()

numbers = [int(n) for n in lines[0].split(',')]

boards = []
for i in range(int((len(lines)-1)/6)):
    boards.append([])
    for j in range(5):
        boards[i].append(lines[1 + 1 + i * 6 + j].split())

boards = np.array(boards).astype('int')

def board_has_won(board, called_numbers):
    called = np.isin(board, called_numbers)
    return np.any(np.all(called, axis=0)) \
        or np.any(np.all(called, axis=1))

def find_losing_board(all_boards, called_numbers):
    losing_boards = np.logical_not(np.array([board_has_won(board, called_numbers) for board in all_boards]))
    losing_indices = losing_boards.nonzero()[0]
    if len(losing_indices) > 0:
        return losing_indices[0]
    return -1

def uncalled_number_sum(board, called_numbers):
    uncalled_numbers = (board[np.logical_not(np.isin(board, called_numbers))]).flatten()
    return sum(uncalled_numbers)

called_numbers = []
last_losing_index = -1
while (losing_index := find_losing_board(boards, called_numbers)) != -1:
    last_losing_index = losing_index
    called_numbers.append(numbers.pop(0))

print("last board to win:", last_losing_index)
print("score:", uncalled_number_sum(boards[last_losing_index], called_numbers) * called_numbers[-1])
