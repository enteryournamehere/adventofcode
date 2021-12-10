opener_table = {')': '(', ']': '[', '}': '{', '>': '<'}
closer_table = {a: b for b, a in opener_table.items()}
error_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_points = {')': 1, ']': 2, '}': 3, '>': 4}

def analyze(line):
    depth = {'(': 0, '[': 0, '{': 0, '<': 0}
    stack = []

    for char in line:
        if char in '([{<':
            stack.append(char)
        else:  # closing
            if stack[-1] == opener_table[char]:
                stack.pop()
            else:
                # INVALID
                return False, error_points[char]

    # time to complete
    completion_score = 0
    stack.reverse()
    for char in stack:
        completion_score *= 5
        completion_score += completion_points[closer_table[char]]
    return True, completion_score

total_error_score = 0
completion_scores = []
with open('input.txt') as file:
    for line in file:
        line = line.strip()
        ok, score = analyze(line)
        if ok:
            completion_scores.append(score)
        else:
            total_error_score += score

print(f'total error score: {total_error_score}')
completion_scores.sort()
print(f'middle completion score: {completion_scores[len(completion_scores) // 2]}')