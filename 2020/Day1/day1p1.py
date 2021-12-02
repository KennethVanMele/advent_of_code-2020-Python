with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

for i in puzzle_input:
    for j in puzzle_input:
        # No redundant checks
        if j == i:
            break

        if i + j == 2020:
            print(i * j)
