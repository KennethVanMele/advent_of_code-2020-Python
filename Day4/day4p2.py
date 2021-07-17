import re

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

all_p.append(cur_p)

passports = []
for p in all_p:
    lines = []
    for line in p:
        lines.append(line.split(" "))
    passports.append(lines)

val = []
for p in passports:
    p = sum(p, [])
    if len(p) == 8:
        val.append(p)
    if len(p) == 7:
        att = []
        for i in p:
            att.append(i.split(":", 1)[0])
        if 'cid' not in att:
            val.append(p)
valid = 0
for v in val:
    checked = 0
    for i in v:
        pref = i.split(":", 1)[0]
        suf = i.split(":", 1)[1]
        if pref == "byr":
            if 1920 <= int(suf) <= 2002:
                checked += 1
        elif pref == "iyr":
            if 2010 <= int(suf) <= 2020:
                checked += 1
        elif pref == "eyr":
            if 2020 <= int(suf) <= 2030:
                checked += 1
        elif pref == "hgt":
            matched = re.match(r'^\d{3}cm$|^\d{2}in$', suf)
            if bool(matched):
                if suf.endswith("cm"):
                    if 150 <= int(suf[0:3]) <= 193:
                        checked += 1
                else:
                    if 59 <= int(suf[0:2]) <= 76:
                        checked += 1
        elif pref == "hcl":
            matched = re.match(r'^#[0-9a-f]{6}', suf)
            if bool(matched) and len(suf) == 7:
                checked += 1
        elif pref == "ecl":
            if suf in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                checked += 1
        elif pref == "pid":
            if len(suf) == 9:
                checked += 1
        # CID is always valid because it is ignored but needs a check + 1 if present.
        else:
            checked += 1

        if checked == len(v):
            valid += 1

print(valid)
