class DeterministicDie:
    next_value = 1
    times_rolled = 0

    def roll(self):
        value = self.next_value
        self.next_value = self.next_value % 100 + 1
        self.times_rolled += 1
        return value

players = []

def someone_has_won():
    for player in players:
        if player[1] >= 1000:
            return True

    return False

with open('input.txt') as file:
    players.append([int(file.readline().strip()[-1]), 0])
    players.append([int(file.readline().strip()[-1]), 0])

die = DeterministicDie()

while not someone_has_won():
    for pi, player in enumerate(players):
        rolls = [die.roll(), die.roll(), die.roll()]
        rolled = sum(rolls)
        player[0] += rolled
        player[0] = (player[0] - 1) % 10 + 1
        player[1] += player[0]

        print(f'Player {pi} rolls {"+".join(str(r) for r in rolls)} and moves to space {player[0]} for a total score of {player[1]}')

        if player[1] >= 1000:
            break

losing_score = players[0][1] if players[0][1] < 1000 else players[1][1]
print(f'die was rolled {die.times_rolled} times')
print(f'losing score {losing_score}')
print(die.times_rolled * losing_score)