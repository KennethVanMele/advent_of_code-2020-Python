with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

acc = 0
line = 0
done = []
while line < len(puzzle_input):
    if line not in done:
        done.append(line)
        if puzzle_input[line].startswith("nop"):
            line += 1
        elif puzzle_input[line].startswith("acc"):
            if puzzle_input[line][4:5] == "+":
                acc += int(puzzle_input[line][5:])
            elif puzzle_input[line][4:5] == "-":
                acc -= int(puzzle_input[line][5:])
            line += 1
        elif puzzle_input[line].startswith("jmp"):
            if puzzle_input[line][4:5] == "+":
                line += int(puzzle_input[line][5:])
            elif puzzle_input[line][4:5] == "-":
                line -= int(puzzle_input[line][5:])
    else:
        break

print(acc)
