with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

ar = []
for i in puzzle_input:
    ar.append(i.split(':'))

pol = []
pw = []
for i in ar:
    pol.append(i[0].split(" "))
    pw.append(i[1])

lb = []
hb = []
ch = []
for i in pol:
    lb.append(int(i[0].split("-")[0]))
    hb.append(int(i[0].split("-")[1]))
    ch.append(i[1])

valid = 0
i = 0
for p in pw:
    if p[lb[i]] == ch[i]:
        if not p[hb[i]] == ch[i]:
            valid += 1
    else:
        if p[hb[i]] == ch[i]:
            valid += 1

    i += 1

print(valid)
