with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

length = len(puzzle_input[0])
po = puzzle_input

for i in range(length):
    c0 = 0
    c1 = 0
    for j in po:
        if j[i] == '0':
            c0 += 1
        else:
            c1 += 1

    if c0 > c1:
        rem = [p for p in po if p[i] == '1']
        for r in rem:
            po.remove(r)
    else:
        rem = [p for p in po if p[i] == '0']
        for r in rem:
            po.remove(r)

    if len(po) == 1:
        break

with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

pc = puzzle_input

for i in range(length):
    c0 = 0
    c1 = 0
    for j in pc:
        if j[i] == '0':
            c0 += 1
        else:
            c1 += 1

    if c0 > c1:
        rem = [p for p in pc if p[i] == '0']
        for r in rem:
            pc.remove(r)
    else:
        rem = [p for p in pc if p[i] == '1']
        for r in rem:
            pc.remove(r)

    if len(pc) == 1:
        break

print(int(''.join(map(str, po)), 2) * int(''.join(map(str, pc)), 2))
