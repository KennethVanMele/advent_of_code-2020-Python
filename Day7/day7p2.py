with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

bags = {}
q = []
for lines in puzzle_input:
    # Clean line from unnecessary words.
    lines = lines.replace('bags', '').replace('bag', '').replace('.', '')

    bag, contains = lines.split('contain')
    bag = bag.strip()

    if 'no other' in contains: # If bag doesn't contain any bag
        bags[bag] = {}
        continue

    contains = contains.split(',')
    contain_dict = {}
    for c in [c.strip() for c in contains]:
        amount = c[:2]
        color = c[2:]
        contain_dict[color] = int(amount)
    bags[bag] = contain_dict


def recursive_count(bag, bags):
    count = 1  # Count the bag itself

    contained_bags = bags[bag]
    for c in contained_bags:
        multiplier = contained_bags[c]
        count += multiplier * recursive_count(c, bags)
    return count


# Minus one to not count the shiny gold bag itself
result = recursive_count('shiny gold', bags) - 1
print(result)
