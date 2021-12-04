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

def find_winning_board(all_boards, called_numbers):
    winning_boards = np.array([board_has_won(board, called_numbers) for board in all_boards])
    winning_indices = winning_boards.nonzero()[0]
    if len(winning_indices) > 0:
        return winning_indices[0]
    return -1

def uncalled_number_sum(board, called_numbers):
    uncalled_numbers = (board[np.logical_not(np.isin(board, called_numbers))]).flatten()
    return sum(uncalled_numbers)

called_numbers = []
while (winning_index := find_winning_board(boards, called_numbers)) == -1:
    called_numbers.append(numbers.pop(0))

print("first board to win:", winning_index)
print("score:", uncalled_number_sum(boards[winning_index], called_numbers) * called_numbers[-1])
