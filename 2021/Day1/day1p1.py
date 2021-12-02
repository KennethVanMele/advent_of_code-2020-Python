with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

s = 0

for i in range(len(puzzle_input)):
    if i - 1 is None:
        break

    if int(puzzle_input[i]) > int(puzzle_input[i - 1]):
        s += 1

print(s)
