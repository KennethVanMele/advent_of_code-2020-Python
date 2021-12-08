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


def is_win(board, row, col):
    board[row][col] = -1
    rs = [int(n) for n in board[row]]
    if sum(rs) == -5:
        return True
    rc = [row[col] for row in board]
    rc = [int(n) for n in rc]
    if sum(rc) == -5:
        return True
    return False


def process_winner(boards, board_indexes):
    for bi, ri, ci in board_indexes:
        board = boards[bi]

        if is_win(board, ri, ci):
            w = [(0 if board[i][j] == -1 else board[i][j]) for i in range(5) for j in range(5)]
            w = [int(n) for n in w]
            return sum(w) * int(num)
    return None


for num in draw:
    score = process_winner(boards, memo[num])

    if score is not None:
        break
print(score)
