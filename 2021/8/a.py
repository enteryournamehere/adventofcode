easy_digit_count = 0
with open('input.txt') as file:
    for line in file:
        parts = line.split('|')
        digits_in = parts[0].split()
        digits_out = parts[1].split()
        for digit in digits_out:
            if len(digit) in [2, 3, 4, 7]:
                easy_digit_count += 1

print(easy_digit_count)