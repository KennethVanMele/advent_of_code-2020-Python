def filter_input(mode):
    with open('input.txt') as inp:
        puzzle_input = [line.strip() for line in inp.readlines()]

    length = len(puzzle_input[0])
    pi = puzzle_input
    if mode == "oxygen":
        p1 = '1'
        p2 = '0'
    elif mode == "co2":
        p1 = '0'
        p2 = '1'

    for i in range(length):
        c0 = 0
        c1 = 0
        for j in pi:
            if j[i] == '0':
                c0 += 1
            else:
                c1 += 1

        if c0 > c1:
            rem = [p for p in pi if p[i] == p1]
            for r in rem:
                pi.remove(r)
        else:
            rem = [p for p in pi if p[i] == p2]
            for r in rem:
                pi.remove(r)

        if len(pi) == 1:
            break

    return pi


po = filter_input("oxygen")
pc = filter_input("co2")
print(int(''.join(map(str, po)), 2) * int(''.join(map(str, pc)), 2))
