# segments
#   αααα
#  β    ψ
#  β    ψ
#   δδδδ
#  ε    φ
#  ε    φ
#   γγγγ
# 
# len 2: 1
# len 3: 7
# len 4: 4
# len 5: 2, 3, 5
# len 6: 0, 6, 9
# len 7: 8

defs = ['αβψεφγ', 'ψφ', 'αψδεγ', 'αψδφγ', 'βψδφ', 'αβδφγ', 'αβδεφγ', 'αψφ', 'αβψδεφγ', 'αβψδφγ']

def do_digit_stuff(digit, meaning, segment_mapping):
    for segment in defs[meaning]:
        segment_mapping[segment] &= set(digit)
    
    for segment in segment_mapping:
        if segment in defs[meaning]:
            continue
        segment_mapping[segment] -= set(digit)

def do_stuff(digits_in, digits_out):
    segment_mapping = {key: set(['a', 'b', 'c', 'd', 'e', 'f', 'g']) for key in ['α', 'β', 'ψ', 'δ', 'ε', 'φ', 'γ']}

    for digit in digits_in:
        if len(digit) == 2:  # 1
            do_digit_stuff(digit, 1, segment_mapping)
        elif len(digit) == 3:  # 7
            do_digit_stuff(digit, 7, segment_mapping)
        elif len(digit) == 4:  # 4
            do_digit_stuff(digit, 4, segment_mapping)
    # print(segment_mapping)

    for digit in digits_in:
        # find zero
        # if β XOR δ is used && ψ AND φ are used && ε AND γ are used
        if  (len((segment_mapping["δ"] | segment_mapping["β"]) & set(digit)) == 1) and \
            (len((segment_mapping["ψ"] | segment_mapping["φ"]) & set(digit)) == 2) and \
            (len((segment_mapping["ε"] | segment_mapping["γ"]) & set(digit)) == 2):
            # zero found
            segment_mapping["β"] &= set(digit)
            segment_mapping["δ"] -= set(digit) 

        # find nine
        if  (len((segment_mapping["δ"] | segment_mapping["β"]) & set(digit)) == 2) and \
            (len((segment_mapping["ψ"] | segment_mapping["φ"]) & set(digit)) == 2) and \
            (len((segment_mapping["ε"] | segment_mapping["γ"]) & set(digit)) == 1):
            # nine found
            segment_mapping["γ"] &= set(digit)
            segment_mapping["ε"] -= set(digit)

        # find six
        if  (len((segment_mapping["δ"] | segment_mapping["β"]) & set(digit)) == 2) and \
            (len((segment_mapping["ψ"] | segment_mapping["φ"]) & set(digit)) == 1) and \
            (len((segment_mapping["ε"] | segment_mapping["γ"]) & set(digit)) == 2):
            # six found
            segment_mapping["φ"] &= set(digit)
            segment_mapping["ψ"] -= set(digit)

    # now we have all segments mapped 1:1
    reverse_map = {key.pop(): value for value, key in segment_mapping.items()}
    def_sets = [set(segments) for segments in defs]

    output = []
    for digit in digits_out:
        real_segments = ''
        for fake_segment in digit:
            real_segments += reverse_map[fake_segment]

        real_segment_set = set(real_segments)
        real_value = def_sets.index(real_segment_set)
        output.append(real_value)

    output = int(''.join(str(digit) for digit in output))
    return output

with open('input.txt') as file:
    total_output = 0
    for line in file:
        parts = line.split('|')
        digits_in = parts[0].split()
        digits_out = parts[1].split()
        output = do_stuff(digits_in, digits_out)
        total_output += output
    print(total_output)
