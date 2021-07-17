with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

# preamble length + 1
line = 6
found = False
while line < len(puzzle_input):
    preamble = puzzle_input[line-5:line-1]
    test = puzzle_input[line]
    for i in preamble:
        for j in preamble:
            if i == j:
                break
            if i + j == test:
                found = False
            else:
                found = True
    if found:
        print(test)
        break
    line += 1
