with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

s = 0

for i in range(len(puzzle_input)):
    try:
        puzzle_input[i + 3]
    except IndexError:
        break

    a = sum([int(puzzle_input[i]), int(puzzle_input[i + 1]), int(puzzle_input[i + 2])])
    b = sum([int(puzzle_input[i + 1]), int(puzzle_input[i + 2]), int(puzzle_input[i + 3])])

    if a < b:
        s += 1

print(s)
