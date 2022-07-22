import sys
input = lambda: sys.stdin.readline().rstrip()

ROW, COL =map(int, input().split())

board = [list(input()) for _ in range(ROW)]
U = (-1, 0)
D = (1, 0)
R = (0, 1)
L = (0, -1)

direction = {'U':[U, R, L], 'D':[D, R, L], 'R':[R, U, D], 'L':[L, U, D],
             U:'U', D:'D', R:'R', L:'L'}

pos = (0, 0)
leaf = 0
for r in range(ROW):
    for c in range(COL):
        if board[r][c] not in ['.', 'o']:
           pos = (r, c)
        elif board[r][c] == 'o':
            leaf += 1


def solve(r, c, remains, ss):
    if remains == 0:
        return print(ss)

    ret = ""

    for tr, tc in direction[board[r][c]]:
        size = 1
        while 0 <= r + tr * size < ROW and 0 <= c + tc * size < COL \
                and board[r+tr*size][c+tc*size] != 'o':
            size += 1
        nr = r + tr * size
        nc = c + tc * size
        if 0 <= nr < ROW and 0 <= nc < COL:
            board[nr][nc] = direction[(tr, tc)]
            tmp = board[r][c]
            board[r][c] = '.'
            solve(nr, nc, remains - 1, ss + direction[(tr, tc)])

            board[r][c] = tmp
            board[nr][nc] = 'o'

    return ret


print(solve(pos[0], pos[1], leaf, ""))
