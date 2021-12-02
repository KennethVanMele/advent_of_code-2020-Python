with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

loc = 0
tree = 0
for i in puzzle_input:
    if i[loc] == '#':
        tree += 1

    for add in range(3):
        loc += 1
        # -1 --> array start @ 0
        if loc > len(i) - 1:
            loc = 0

print(tree)
