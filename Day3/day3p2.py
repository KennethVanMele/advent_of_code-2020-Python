with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]


def check_tree(f_input, step):
    f_loc = 0
    tree = 0
    for i in f_input:
        if i[f_loc] == '#':
            tree += 1

        for add in range(step):
            f_loc += 1
            # -1 --> array start @ 0
            if f_loc > len(i) - 1:
                f_loc = 0

    return tree


# first slope
tree1 = check_tree(puzzle_input, 1)
tree2 = check_tree(puzzle_input, 3)
tree3 = check_tree(puzzle_input, 5)
tree4 = check_tree(puzzle_input, 7)

# fifth slope
loc = 0
tree5 = 0
# Skip every second row
skip = False
for i in puzzle_input:
    if skip:
        skip = False
        continue
    else:
        skip = True

    if i[loc] == '#':
        tree5 += 1

    loc += 1
    if loc > len(i) - 1:
        loc = 0

print(tree1 * tree2 * tree3 * tree4 * tree5)
