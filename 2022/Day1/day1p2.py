with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

elfs = []
curr_call = 0

try:
    for i in puzzle_input:
        if i != '':
            curr_call += int(i)
        else:
            elfs.append(curr_call)
            curr_call = 0
# Fix read last line
finally:
    elfs.append(curr_call)

elfs.sort(reverse=True)
print((elfs[0]+elfs[1]+elfs[2]))
