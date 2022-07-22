import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
cache = [[[-1] * C for _ in range(R)] for _ in range(4)]

mU, mR, mD, mL = (-1, 0), (0, 1), (1, 0), (0, -1)

move = [[mD, mR], [mU, mL], [mD, mR]]


def solve(stage, r, c):
    if stage == 0 and r == R-1 and c == C-1:
        return solve(stage+1, r, c)
    elif stage == 1 and r == 0 and c == 0:
        return solve(stage+1, r, c)
    elif stage == 2 and r == R-1 and c == C-1:
        return board[r][c]

    if cache[stage][r][c] != -1:
        return cache[stage][r][c]

    tmp = board[r][c]
    board[r][c] = 0
    cache[stage][r][c] = 0

    for tr, tc in move[stage]:
        nr = r + tr
        nc = c + tc

        if 0 <= nr < R and 0 <= nc < C:
            cache[stage][r][c] = max(cache[stage][r][c],
                                     tmp + solve(stage, nr, nc))

    board[r][c] = tmp
    return cache[stage][r][c]


print(solve(0, 0, 0))
print()