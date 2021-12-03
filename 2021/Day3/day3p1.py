with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

gamma = []
epsilon = []

for i in range(len(puzzle_input[0])):
    c0 = 0
    c1 = 0
    for j in puzzle_input:
        if j[i] == '0':
            c0 += 1
        else:
            c1 += 1

    if c0 > c1:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

print(int(''.join(map(str, gamma)), 2) * int(''.join(map(str, epsilon)), 2))
