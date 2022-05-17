move = {0:(0, 1), 1: (1, 0), 2:(0, -1), 3:(-1, 0)}

def solution(grid):
    answer = []

    board = [list(g) for g in grid]
    row, col, direction = len(board), len(board[0]), 4
    visit = [[[False] * col for _ in range(row)] for _ in range(direction)]
    # [direction][row][col]

    for r in range(row):
        for c in range(col):
            for d in range(direction):
                if not visit[d][r][c]:
                    count = 0
                    while not visit[d][r][c]:
                        visit[d][r][c] = True
                        count += 1
                        dr, dc = move[d]
                        r = (r + dr + row) % row
                        c = (c + dc + col) % col
                        if board[r][c] != "S":
                            if board[r][c] == "L":
                                d = (d + len(move) + 1) % len(move)
                            elif board[r][c] == "R":
                                d = (d + len(move) - 1) % len(move)

                    answer.append(count)


    return sorted(answer)


# grid = ["SL", "LR"]
# print(solution(grid))
# grid = ["S"]
# print(solution(grid))
grid = ["R", "R"]
print(solution(grid))
