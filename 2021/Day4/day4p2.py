with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

draw = puzzle_input[0]
draw = draw.split(",")
board = []
boards = []
found = False
score = 0

for i in range(len(puzzle_input)):
    row = []
    if i < 2 or len(puzzle_input[i]) == 0:
        continue
    else:
        row = puzzle_input[i].split(" ")
        row = list(filter(None, row))
        board.append(row)
        if len(board) == 5:
            boards.append(board)
            board = []

for i in draw:
    for b in boards:
        for r in b:
            if r.__contains__(i):
                r.remove(i)
            if len(r) == 0:
                boards.remove(b)

            if len(boards) == 1:
                for fr in b:
                    print(b)
                    fr = [int(n) for n in fr]
                    score += sum(fr)
                found = True

    if found:
        print(score)
        score = score * int(i)
        print(score)
        break
