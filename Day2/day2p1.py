with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

ar = []
for i in puzzle_input:
    ar.append(i.split(':'))

# Split policy and password
pol = []
pw = []
for i in ar:
    pol.append(i[0].split(" "))
    pw.append(i[1])

# Split policy in lowbound, highbound and character
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
    if not p.count(ch[i]) < lb[i] and not p.count(ch[i]) > hb[i]:
        valid += 1

    i += 1

print(valid)
