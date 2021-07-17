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

all_yes = 0
for form in all_f:
    occurrence = {}
    for line in form:
        for ch in line:
            # Make new key/value if key not present
            if ch not in occurrence:
                occurrence[ch] = 0
            # Add 1 if key present
            occurrence[ch] += 1

    # Get number of people in form
    num_p = len(form)
    for val in occurrence.values():
        # We only want where they all voted yes
        if val == num_p:
            all_yes += 1

print(all_yes)
