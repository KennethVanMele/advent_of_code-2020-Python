with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

to_check = ["shiny gold"]

# For-loops work with growing lists. Each bag has to be checked for each line!
for bag in to_check:
    for line in puzzle_input:
        if str(bag) in line:
            # Get the first 2 words of the line
            new_bag = ' '.join(line.split(" ")[0:2])
            if new_bag not in to_check:
                to_check.append(new_bag)

# You don't need the original bag so - 1
print(len(to_check) - 1)
