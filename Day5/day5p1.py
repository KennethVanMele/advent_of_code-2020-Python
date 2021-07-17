from statistics import median
from math import floor, ceil
with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

sids = []
for line in puzzle_input:
    rlb = 0
    rhb = 127
    r = range(rlb, rhb)
    row = 0
    # Get row
    for ri in line[:7]:
        if ri == 'F':
            rhb = floor(median(r))
            r = range(rlb, rhb)
            rval = rhb
        else:
            rlb = ceil(median(r) + 1)
            r = range(rlb, rhb)
            rval = rlb

    row = rval

    clb = 0
    chb = 7
    c = range(clb, chb)
    col = 0
    for ci in line[7:]:
        if ci == 'L':
            chb = floor(median(c))
            c = range(clb, chb)
            cval = chb
        else:
            clb = ceil(median(c) + 1)
            c = range(clb, chb)
            cval = clb

    col = cval

    sid = row * 8 + col
    sids.append(sid)

print(max(sids))
