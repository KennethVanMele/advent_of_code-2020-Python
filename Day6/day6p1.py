with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

cur_f = []
all_f = []
for item in puzzle_input:
    if item == '':
        all_f.append(cur_f)
        cur_f = []
    else:
        cur_f.append(item)

all_f.append(cur_f)

a_yes = []
total_yes = []
for form in all_f:
    for line in form:
        for i in line:
            if i not in a_yes:
                a_yes.append(i)

    total_yes.append(len(a_yes))
    a_yes = []

print(sum(total_yes))
