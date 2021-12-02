with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

ar = []
for i in puzzle_input:
    ar.append(i.split(" "))


direction = []
distance = []
for i in ar:
    direction.append(i[0])
    distance.append(i[1])

horizontal = 0
depth = 0
aim = 0
for i in range(len(direction)):
    if direction[i] == "forward":
        horizontal += int(distance[i])
        depth += aim * int(distance[i])
    elif direction[i] == "down":
        aim += int(distance[i])
    else:
        aim -= int(distance[i])

print(horizontal * depth)
