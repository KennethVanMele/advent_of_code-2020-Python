with open('input.txt') as inp:
    puzzle_input = [line.strip() for line in inp.readlines()]

draw = puzzle_input[0]
draw = draw.split(",")
board = []
boards = []
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

memo = {}
for num in draw:
    memo[num] = []
for bi, board in enumerate(boards):
    for ri, row in enumerate(board):
        for ci, num in enumerate(row):
            if num in memo:
                memo[num].append((bi, ri, ci))


def is_win(grid, row, col):
    grid[row][col] = -1
    rs = [int(n) for n in grid[row]]
    if sum(rs) == -5:
        return True
    rc = [row[col] for row in grid]
    rc = [int(n) for n in rc]
    if sum(rc) == -5:
        return True
    return False


def process_winner(grids, grid_indexes):
    for gi, ri, ci in grid_indexes:
        grid = grids[gi]

        if is_win(grid, ri, ci):
            w = [(0 if grid[i][j] == -1 else grid[i][j]) for i in range(5) for j in range(5)]
            w = [int(n) for n in w]
            return sum(w) * int(num)
    return None


for num in draw:
    score = process_winner(boards, memo[num])

    if score is not None:
        break
print(f'Answer: {score}')
