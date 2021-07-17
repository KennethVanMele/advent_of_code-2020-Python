with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

cur_p = []
all_p = []
for item in puzzle_input:
    if item == '':
        all_p.append(cur_p)
        cur_p = []
    else:
        cur_p.append(item)

# last line isn't empty
all_p.append(cur_p)

passports = []
for p in all_p:
    lines = []
    for line in p:
        lines.append(line.split(" "))
    passports.append(lines)

valid = 0
for p in passports:
    # merge all sub arrays in passport
    p = sum(p, [])
    if len(p) == 8:
        valid += 1
    # CID can be ignored
    if len(p) == 7:
        att = []
        for i in p:
            att.append(i.split(":", 1)[0])
        if 'cid' not in att:
            valid += 1

print(valid)
